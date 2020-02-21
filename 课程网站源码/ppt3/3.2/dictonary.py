# -*- coding: utf-8 -*-
if __name__ == "__main__":
    dict = {}
    dict["one"] = "1 - 慕课网-程序员的梦工厂"
    dict[2] = "2 - 慕课网-程序员的梦工厂"

    tinydict = { "name":"imooc","code":1 ,"site":"www.imooc.com" }
    print( dict )
    print( dict[ "one" ] )
    print( dict[ 2 ] )
    print( tinydict )
    print( tinydict.keys() )
    print( tinydict.values() )