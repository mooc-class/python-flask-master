# -*- coding: utf-8 -*-
from application import app,db
from flask import Blueprint,render_template,request,jsonify
from common.libs.Helper import ops_renderJSON,ops_renderErrJSON
from common.libs.DataHelper import getCurrentTime
from common.models.user import User
from common.libs.UserService import UserService

member_page = Blueprint( "member_page",__name__ )

@member_page.route("/reg",methods = [ "GET","POST" ])
def reg():
    if request.method == "GET":
        return render_template("member/reg.html")

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


@member_page.route("/login")
def login():
    return render_template("member/login.html")

