# hello_c

A dummy project for experimenting on distribution of ctypes-based
python module 

Manual build (note, the generated wheel contains the `_c_api-*.so`):

```
python -m build
```

Install:

```
pip install dist/hello_c-<VERSION>.whl
```

Usage:

```python
from hello_c import c_api

c_api.hello_c()
c_api.hell2_c()
```


# TODO
- use cibuildwheel to auto-build wheels for manylinux and arm64 / amd64