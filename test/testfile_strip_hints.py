#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

Testfile for stripping hints.

"""

from __future__ import print_function, division, absolute_import

# Some of below tests are based on ones here:
# https://stackoverflow.com/questions/42733877/remove-type-hints-in-python-source-programmatically


e : int = lambda x,y,z: lambda: 4*(3+3)

"""Triple string"""

xxx: int
xxx: list = ggg
print(xxx); print(e)

# Below line raises an exception.  Need to insert a backslash to fix it, see code note.
#tree: Dict[t
#        ] = 4

chair: Dict[W] = [1,  # c1
                  2]  # c2

def default_combine_chars_fun_ZZ(elem_list: List[float], egg: int=4) -> List[str]: # TODO: remove annotations test
    pass

def in_fun():
    e=3
    e=3 # comment
    xxx: int
    xxx: int # comment
    xxx : list = ggg
    xxx : list = ggg # comment
    print(xxx)
    var : int = 4; var2 : int =34

@decorator
def foo(bar: Dict[T, List[T]], # comment
        baz: Callable[[T], int] = 444 + 4, # comment
        **kwargs) -> List[T]: # comment
    pass

def foo(bar: Dict[T, List[T]]):
    pass

def foo(bar: Dict[T, List[T]],):
    pass

def foo(bar: Dict[T, List[T]],
        baz: Callable[[T], int] = lambda x, y: (x+3)/7,
        **kwargs) -> List[T]:
    pass

