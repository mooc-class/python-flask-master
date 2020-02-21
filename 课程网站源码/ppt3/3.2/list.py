# -*- coding: utf-8 -*-
if __name__ == "__main__":
    list = [ "abcd",786,2.23,"imooc",70.2 ]
    tinylist = [ 123,"imooc"]
    print( list )
    print( list[0] )
    print( list[1:3] )
    print( list[2:] )
    print( tinylist * 2 )
    print( list + tinylist )

    tinylist.append( "456" )
    print(tinylist)