# -*- coding: utf-8 -*-
from application import app
from indexController import index_page
from postController import post_page

app.register_blueprint( index_page,url_prefix = "/imooc" )
app.register_blueprint( post_page,url_prefix = "/post" )