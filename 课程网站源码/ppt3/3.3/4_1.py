# -*- coding: utf-8 -*-

class Student(object):
    def __init__(self,name,score):
        self.name = name
        self.__score = score

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self,score):
        if score < 0 or score > 100:
            raise  ValueError( "invalid score" )
        self.__score = score

s = Student( "imooc","100" )
s.score = 101
print( s.score )