# -*- coding: utf-8 -*-
from flask import Flask

from flask_sqlalchemy import SQLAlchemy
app = Flask( __name__ )

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:123456@127.0.0.1/mysql"
db = SQLAlchemy( app )



