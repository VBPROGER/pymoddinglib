#!/usr/bin/env python3
try: # version >= 3.4
    import importlib
    PY_MAGIC = importlib.util.MAGIC_NUMBER
except BaseException:
    import imp
    PY_MAGIC = imp.get_magic()

FILE_FORMAT_PML = '.pml' # PyModdingLib
FILE_FORMAT_PYC = '.pmlm' # PyModdingLib Mod
FILE_FORMAT_SOURCE = '.pmls' # PyModdingLib Source

if __name__ == '__main__':
    print(PY_MAGIC)
    print(PY_MAGIC.hex())
    print(FILE_FORMAT_PML, FILE_FORMAT_PYC, FILE_FORMAT_SOURCE)
