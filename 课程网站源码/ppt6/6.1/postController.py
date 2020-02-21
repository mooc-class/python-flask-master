# -*- coding: utf-8 -*-
from flask import Flask,Blueprint
'''
post/index 列表
post/info 详情
post/set 添加|编辑
post/ops 操作（删除|恢复）
'''

post_page = Blueprint( "post_page",__name__ )

@post_page.route( "/index" )
def index():
    return "post index"


@post_page.route( "/info" )
def info():
    return "post info"

