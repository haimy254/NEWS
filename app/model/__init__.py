from ensurepip import bootstrap
from flask import Flask
from app.config import DevConfig
from flask_bootstrap import Bootstrap
from app import app
from app import views
from app import error

app=Flask(__name__,instance_relative_config = True)
app.config.from_object(DevConfig) 
app.config.from_pyfile('config.py')

bootstrap =Bootstrap(app)


