from flask import render_template
from .request import get_news
from app import app 

@app.route('/')
def index():
    
    popular_news= get_news('popular')
    print(popular_news)
    title = 'home - Welcome to current world wide news website online'
    return render_template('index.html', title = title,popular = popular_news)