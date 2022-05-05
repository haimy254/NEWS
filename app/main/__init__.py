
from flask import Flask
from ..config import DevConfig
from flask_bootstrap import Bootstrap

bootstrap =Bootstrap()

app=Flask(__name__)
app.config.from_object(DevConfig) 
app.config.from_pyfile('config.py')



from app.main import views
from app.main import error

