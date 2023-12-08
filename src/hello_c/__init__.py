from ctypes import cdll
from importlib.util import find_spec

try:
    c_api = cdll.LoadLibrary(find_spec("hello_c._c_api").origin)
except Exception as e:
    raise ImportError from e
