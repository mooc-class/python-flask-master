# -*- coding: utf-8 -*-
from flask import Flask
app = Flask( __name__ )

@app.route( "/" )
def hello():
    return "Hello ,I Love Imooc"

@app.route( "/my/<user_name>" )
def my( user_name ):
    return "my page:user %s" %( user_name )

if __name__ == "__main__":
    app.run( host = "0.0.0.0",debug=True )