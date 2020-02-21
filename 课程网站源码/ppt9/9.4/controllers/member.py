# -*- coding: utf-8 -*-
from application import app,db
from flask import Blueprint,request,make_response,redirect
from common.libs.Helper import ops_renderJSON,ops_renderErrJSON,ops_render
from common.libs.DataHelper import getCurrentTime
from common.libs.UrlManager import UrlManager
from common.models.user import User
from common.libs.UserService import UserService

member_page = Blueprint( "member_page",__name__ )

@member_page.route("/reg",methods = [ "GET","POST" ])
def reg():
    if request.method == "GET":
        return ops_render("member/reg.html")

    req = request.values
    nickname = req['nickname'] if "nickname" in req else ""
    login_name = req['login_name'] if "login_name" in req else ""
    login_pwd = req['login_pwd'] if "login_pwd" in req else ""
    login_pwd2 = req['login_pwd2'] if "login_pwd2" in req else ""

    if login_name is None or len( login_name ) < 1:
        return ops_renderErrJSON( msg = "请输入正确的登录用户名~~" )

    if login_pwd is None or len( login_pwd ) < 6:
        return ops_renderErrJSON( msg ="请输入正确的登录密码，并且不能小于6个字符~~")

    if login_pwd != login_pwd2:
        return ops_renderErrJSON(msg="请输入正确的确认登录密码~~")

    user_info = User.query.filter_by( login_name = login_name ).first()
    if user_info:
        return ops_renderErrJSON( msg ="登录用户名已被注册，请换一个~~")

    model_user = User()
    model_user.login_name = login_name
    model_user.nickname = nickname if nickname is not None else login_name
    model_user.login_salt = UserService.geneSalt( 8 )
    model_user.login_pwd = UserService.genePwd( login_pwd,model_user.login_salt )
    model_user.created_time = model_user.updated_time = getCurrentTime()
    db.session.add( model_user )
    db.session.commit()
    return ops_renderJSON( msg = "注册成功~~" )


@member_page.route("/login",methods = [ "GET","POST" ])
def login():
    if request.method == "GET":
        return ops_render("member/login.html")

    req = request.values
    login_name = req['login_name'] if 'login_name' in req else ''
    login_pwd = req['login_pwd'] if 'login_pwd' in req else ''
    if login_name is None or len( login_name ) < 1:
        return ops_renderErrJSON(  "请输入正确的登录用户名~~" )

    if login_pwd is None or len( login_pwd ) < 6:
        return ops_renderErrJSON("请输入正确的登录密码~~")
    user_info = User.query.filter_by( login_name = login_name ).first()
    if not user_info:
        return ops_renderErrJSON("请输入正确的登录用户名和密码 -1~~")

    if user_info.login_pwd != UserService.genePwd( login_pwd,user_info.login_salt ):
        return ops_renderErrJSON("请输入正确的登录用户名和密码 -2 ~~")

    if user_info.status != 1:
        return ops_renderErrJSON( "账号被禁用，请联系管理员处理~~" )

    #session['uid'] = user_info.id
    response = make_response( ops_renderJSON( msg="登录成功~~" ) )
    response.set_cookie(app.config['AUTH_COOKIE_NAME'],
                        "%s#%s"%( UserService.geneAuthCode( user_info ),user_info.id ),60 * 60 *24 *120 )
    return response


@member_page.route("/logout")
def logOut():
    response = make_response( redirect( UrlManager.buildUrl("/") ) )
    response.delete_cookie(  app.config['AUTH_COOKIE_NAME'] )
    return response


