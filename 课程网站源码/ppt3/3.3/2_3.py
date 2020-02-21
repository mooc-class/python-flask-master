# -*- coding: utf-8 -*-
import functools
def use_logging( level = "debug" ):
    def decorator(func):
        @functools.wraps( func )
        def wrapper( *args,**kwargs ):
            print("[%s] %s is running" % ( level,func.__name__) )
            return func( *args,**kwargs )

        return wrapper
    return decorator


def bar():
    print('i am bar')

def bar2():
    print('i am bar2')

f = use_logging( level = "info" )( bar )
f()
print( f.__name__ )
print( f.__doc__ )
