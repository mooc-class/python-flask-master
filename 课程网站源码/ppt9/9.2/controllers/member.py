# -*- coding: utf-8 -*-
from application import app
from flask import Blueprint,render_template
member_page = Blueprint( "member_page",__name__ )

@member_page.route("/reg")
def reg():
    return render_template("member/reg.html")


@member_page.route("/login")
def login():
    return render_template("member/login.html")

