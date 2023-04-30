#!/usr/bin/env python3
def Meta(Data):
    global Information
    Information = Data['PyAssemblyInformation']()
    Information['AssemblyName'] = 'simpletemplate'
    Information['AssemblyDescription'] = 'A template for your mod'
    Information['AssemblyVersion'] = '1.0.0'
def Main():
    print('Mod Loaded') # Enter your code here