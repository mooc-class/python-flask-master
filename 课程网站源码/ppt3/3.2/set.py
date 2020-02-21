# -*- coding: utf-8 -*-
if __name__ == "__main__":
    student = { "Tom","Jim","Mary","Tom","Jack","Rose" }
    print( student )
    if "Rose" in student:
        print( "Rose在集合中" )
    else:
        print("Rose不在集合中")

    a = set( "abrasdfasdfs" )
    b = set( "sdafwerdfd" )
    print( a )
    print( b )
    print( a - b )
    print( a | b )
    print( a & b )
    print( a ^ b )