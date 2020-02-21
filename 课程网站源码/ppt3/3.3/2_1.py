# -*- coding: utf-8 -*-
def use_logging( level = "debug" ):
    def decorator(func):
        def wrapper( *args,**kwargs ):
            print("[%s] %s is running" % ( level,func.__name__) )
            return func( *args,**kwargs )

        return wrapper
    return decorator

@use_logging( level = "info" )
def bar():
    print('i am bar')

@use_logging( level = "warn" )
def bar2():
    print('i am bar2')

bar()
bar2()
