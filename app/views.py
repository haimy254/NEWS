
from flask import render_template
from .request import get_news1,get_news2
from app import app 


@app.route('/news/<int:id>')
def index(id):
    news = get_news1(id)
    title = f'{news.title}'
  
    return render_template('index.html', title = title,news = news )