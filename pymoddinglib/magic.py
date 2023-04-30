#!/usr/bin/env python3
try: # version >= 3.4
    import importlib
    PY_MAGIC = importlib.util.MAGIC_NUMBER
except BaseException:
    import imp
    PY_MAGIC = imp.get_magic()

FILE_FORMAT_PML = '.pml' # PyModdingLib
FILE_FORMAT_PYC = '.pmlm' # PyModdingLib Mod

if __name__ == '__main__':
    print(PY_MAGIC)
    print(PY_MAGIC.hex())
