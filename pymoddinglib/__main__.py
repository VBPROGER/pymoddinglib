#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import __init__ as pml
App = pml.ModdableApp('MyApp', {}, True, True)
# print(App.mods)
# App.set_mod_name('modname', 'author', 'hahaha')
# print(App.mods)
# App.set_mod_author('mymod', 'user', 'oops')
# print(App.mods)
print(App.get_mod_module('mymod', 'user').Information)
App.run_mods()
# App.run_mods(ignore_disabled = True)