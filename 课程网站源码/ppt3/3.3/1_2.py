# -*- coding: utf-8 -*-
def use_logging( func ):
    #print( "[debug] " + func_name + " is running")
    def wrapper( *args,**kwargs ):
        print("[debug] %s is running" % func.__name__ )
        return func( *args,**kwargs )

    return wrapper

def bar():
    print('i am bar')

def bar2():
    print('i am bar2')

bar = use_logging( bar )
bar()

bar2 = use_logging( bar2 )
bar2()
