# -*- coding: utf-8 -*-
from flask import Flask

app = Flask( __name__ )
app.config.from_envvar( "ops_config" )
@app.route( "/" )
def hello():
    return "Hello, I Love Imooc "

if __name__ == "__main__":
    app.run( host = "0.0.0.0" )
    #app.run()