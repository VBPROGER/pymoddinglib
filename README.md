# PyModdingLib
This library adds a modding support to Python.
## Starting module directly
You can start module directly by using this code:
```python3
from pydoc import importfile
Mod = importfile('simpletemplate.pmlm')
print(Mod)
Mod.Main()
```
However, it has some issues. For example, let's try calling the function `Meta`:
```
Mod.Meta()
```
You will need to pass arguments to this functions, so you can't use it directly.
