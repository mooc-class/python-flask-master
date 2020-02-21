# -*- coding: utf-8 -*-
from application import db
class User( db.Model ):
    Host = db.Column( db.String( 80 ),primary_key=True )
    User = db.Column( db.String( 120 ) )