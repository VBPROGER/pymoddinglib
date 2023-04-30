#!/usr/bin/env python3
def Meta(Data):
    global Information
    Information = Data['PyAssemblyInformation']()
    Information['AssemblyName'] = 'mymod'
    Information['AssemblyDescription'] = 'A testing mod'
    Information['AssemblyVersion'] = '1.0.1'
def Main():
    print('Hello World!')
    sup = str(input('What\'s up?\n')).strip().lower()
    if 'fine' in sup or 'good' in sup: print('Nice!')
    else: print('Wish you good luck!')
    print('Finished running')

if __name__ == '': print('You are launching me as file. Please import me as library instead. (I\'m a mod!)')
