__all__ = []

#Copied from stack overflow to handle dynamic import of all bots from bots folder
#Should see proper refactor when I can get my head around it.

import pkgutil
import inspect

for loader, name, is_pkg in pkgutil.walk_packages(__path__):
    module = loader.find_module(name).load_module(name)

    for name, value in inspect.getmembers(module):
        if name.startswith('__'):
            continue

        globals()[name] = value
        __all__.append(name)