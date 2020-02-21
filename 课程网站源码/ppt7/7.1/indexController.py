# -*- coding: utf-8 -*-
from flask import Flask,Blueprint,request,make_response,jsonify,render_template
from sqlalchemy import  text
from application import db

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


@index_page.route("/get")
def get():
    #var_a = request.args.get( "a","i love imooc" )
    ##变种
    req = request.values
    var_a = req['a'] if "a" in req else "i love imooc"
    return "request:%s,params:%s,var_a:%s"%(request.method,request.args,var_a )

@index_page.route("/post",methods = [ "POST" ])
def post():
    #三元表达式
    #var_a = request.form['a'] if "a" in request.form else 'i love imooc'
    #普通容易看懂的
    # var_a = ""
    # if "a" in request.form:
    #     var_a = request.form['a']
    ##变种
    req = request.values
    var_a = req['a'] if "a" in req else "i love imooc"
    return "request:%s,params:%s,var_a:%s"%( request.method,request.form,var_a )

@index_page.route("/upload",methods = [ "POST" ])
def upload():
    f = request.files['file'] if "file" in request.files else None
    return "request:%s,params:%s,file:%s"%(request.method,request.files,f )


@index_page.route("/text")
def text_a():
    return "text/html"

@index_page.route("/text_same")
def text_same():
    response = make_response( "text/html",200 )
    return response


@index_page.route("/json")
def json():
    import json
    data = { "a":"b" }
    response = make_response( json.dumps( data ) )
    response.headers["Content-Type"] = "application/json"
    return response

@index_page.route( "/json_same" )
def json_same():
    data = { "a":"b" }
    response = make_response( jsonify( data )  )
    return response

@index_page.route("/template")
def template():
    ##传值
    name = "imooc"
    ##
    context = { "name" : name }
    context['user'] = { "nickname":"编程浪子","qq":"xxxxx","home_page":"http://www.54php.cn" }
    context['num_list'] = [ 1,2,3,4,5]


    ##查询数据库
    sql = text( "select * from `user`")
    result = db.engine.execute( sql )
    context['result'] = result
    #return render_template( "index.html",name = name )
    return render_template( "index.html",**context )


@index_page.route("/extend_template")
def extend_template():
    return render_template( "extend_template.html" )


@index_page.route("/extend_template_other")
def extend_template_other():
    return render_template( "extend_template_other.html" )


