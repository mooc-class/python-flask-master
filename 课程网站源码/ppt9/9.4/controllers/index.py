# -*- coding: utf-8 -*-
from flask import Blueprint,render_template
from common.models.user import User
from application import app
from common.libs.Helper import ops_render
index_page = Blueprint( "index_page",__name__ )

@index_page.route("/")
def index():
    ##传值
    name = "imooc"
    ##
    context = { "name" : name }
    context['user'] = { "nickname":"编程浪子","qq":"xxxxx","home_page":"http://www.54php.cn" }
    context['num_list'] = [ 1,2,3,4,5]

    result = User.query.all()
    context['result'] = result

    #app.logger.info( session['uid'] )

    return ops_render( "index.html",context )
