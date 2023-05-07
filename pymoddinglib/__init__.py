#!/usr/bin/env python3
from typing import Any
from pydoc import importfile as import_file
from datetime import datetime
from pymoddinglib import magic
import os.path as path

__name__ = 'pymoddinglib'
__version__ = '1.0.0'

class MainError(BaseException): 'Base class for all errors.'
class AssemblyError(MainError): 'Assembly error.'
class SecurityError(MainError): 'Security violation error.'
class PyAssemblyInformation:
    AssemblyName: str
    AssemblyVersion: str
    AssemblyDescription: str
    AssemblyAuthor: str
    AssemblyCompany: str
    AssemblyDate: int
    AssemblyLicense: str
    AssemblyOrganizationType: str
    def __init__(self, *args, **kwargs):
        self.AssemblyName = 'None'
        self.AssemblyVersion = '1.0.0'
        self.AssemblyDescription = 'This program has no description.'
        self.AssemblyAuthor = 'Unknown'
        self.AssemblyDate = int(datetime.now().year)
        self.AssemblyLicense = 'Unknown'
        self.AssemblyOrganizationType = 'com'
        for arg in kwargs:
            value = kwargs[arg]
            self.__setattr__(arg, value)
    def __str__(self):
        from json import dumps as dumpstring
        return dumpstring(self.__dict__)
    def __getitem__(self, item: str = 'AssemblyName'): return self.__getattr__(item)
    def __setitem__(self, item: str = 'AssemblyName', value: any = 'None'):
        item = str(item).title().strip()
        if not item.startswith('Assembly'): raise SecurityError('Value out of bounds; should start with "Assembly"')
        return self.__setattr__(item, value)
    def _normalize(self, s: str = ''): return s.lower().strip() or 'unknown'
    @property
    def AssemblyID(self):
        return '{}.{}.{}_{}'.format(self._normalize(self.AssemblyOrganizationType), self._normalize(self.AssemblyCompany), self._normalize(self.AssemblyName), self.AssemblyVersion.strip())
class ModdableApp:
    def __init__(self, name: str, obj, autoscan: bool = False, autoenable: bool = False, *args, **kwargs):
        self.name, self.app = name, obj
        self.mods_folder = 'mods'
        self.split_symbol = '.'
        self.mods = {}
        for arg in kwargs:
            value = kwargs[arg]
            self.__setattr__(arg, value)
        if autoscan: self.scan_and_parse_mods()
        if autoenable: self.enable_all()
    def __call__(self, *args: Any, **kwds: Any) -> Any: pass
    def scan_for_mods(self):
        from os import listdir
        return listdir(self.mods_folder)
    def parse_mods(self, modlist: list = [], add_dict: bool = False):
        moddict = {}
        for mod in modlist:
            mod_s = mod.split(self.split_symbol)
            moddict[mod] = {
                'name': mod_s[1],
                'author': mod_s[0],
                'state': False
            }
        if add_dict: self.mods = moddict
        return moddict
    def scan_and_parse_mods(self): self.parse_mods(self.scan_for_mods(), True)
    def set_mod_meta(self, name: str, author: str, meta: str, value: any): self.mods[self.generate_mod_name(name, author)][meta] = value
    def set_mod_name(self, name: str, author: str, new_name: str):
        self.set_mod_meta(name, author, 'name', new_name)
        self.mods[self.generate_mod_name(new_name, author)] = self.get_mod(name, author)
        del self.mods[self.generate_mod_name(name, author)]
    def set_mod_author(self, name: str, author: str, new_author: str):
        self.set_mod_meta(name, author, 'author', new_author)
        self.mods[self.generate_mod_name(name, new_author)] = self.get_mod(name, author)
        del self.mods[self.generate_mod_name(name, author)]
    def set_mod_state(self, name: str, author: str, state: bool = False): self.set_mod_meta(name, author, 'state', state)
    def set_mod_enabled(self, name: str, author: str): self.set_mod_state(name, author, True)
    def set_mod_disabled(self, name: str, author: str): self.set_mod_state(name, author, False)
    def get_mod(self, name: str, author: str) -> dict: return self.mods[self.generate_mod_name(name, author)]
    def generate_mod_name(self, name: str, author: str) -> str: return author + self.split_symbol + name
    def get_modpath(self, name: str, author: str):
        return path.join(self.mods_folder, self.generate_mod_name(name, author), name + magic.FILE_FORMAT_PYC)
    def run_mod(self, name: str, author: str, start: bool = True, grant_meta: bool = True, ignore_disabled: bool = False, ignore_incorrect_format: bool = False, ignore_incorrect_magic: bool = False) -> bool or any:
        full_modname = self.generate_mod_name(name, author)
        full_modpath = self.get_modpath(name, author)
        with open(full_modpath, 'rb+') as f: data = f.read()
        if not ignore_disabled:
            if not self.get_mod(name, author)['state']: return False
        if not ignore_incorrect_format:
            if not check_file_format(full_modpath): raise AssemblyError('Invalid file format')
        if not ignore_incorrect_magic:
            if not check_is_bytecode(data): raise AssemblyError('Incorrect magic')
        mod = import_file(full_modpath)
        if grant_meta: mod.Meta(InformationForMods)
        if start: mod.Main()
        return mod
    def run_mods(self, *args, **kwargs):
        for mod in self.mods:
            key = self.mods[mod]
            self.run_mod(key['name'], key['author'], *args, **kwargs)
    def extract_mod_data_from_name(self, fullname: str) -> dict:
        splitted = fullname.split(self.split_symbol)
        data = {
            'name': splitted[1],
            'author': splitted[0]
        }
        return data
    def mod_data_to_tuple(self, mod_data: dict) -> tuple: return tuple([mod_data['name'], mod_data['author']])
    def enable_all(self):
        for mod in self.mods: self.set_mod_enabled(*self.mod_data_to_tuple(self.extract_mod_data_from_name(mod)))
    def disable_all(self):
        for mod in self.mods: self.set_mod_disabled(*self.mod_data_to_tuple(self.extract_mod_data_from_name(mod)))
    def get_mod_module(self, name: str, author: str): return self.run_mod(name, author, False)
def check_is_bytecode(content: bytes or bytearray) -> bool:
    return content.startswith(magic.PY_MAGIC)
def check_file_format(filename: str) -> bool:
    return filename.endswith(magic.FILE_FORMAT_PYC)
def get_fields(imported_module) -> PyAssemblyInformation:
    try:
        information = imported_module.Information
        if type(information) == PyAssemblyInformation: return information
        raise AssemblyError('Invalid information')
    except AttributeError:
        raise AssemblyError('Missing information')

InformationForMods = {
    'PyAssemblyInformation': PyAssemblyInformation
}
