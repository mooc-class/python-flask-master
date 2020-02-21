# -*- coding: utf-8 -*-
from flask import Flask,Blueprint
'''
post/index 列表
post/info 详情
post/set 添加|编辑
post/ops 操作（删除|恢复）
'''

index_page = Blueprint( "index_page",__name__ )

@index_page.route( "/" )
def index_page_index():
    return "index page"


@index_page.route( "/me" )
def hello():
    return "hello ,I Love Imooc"

