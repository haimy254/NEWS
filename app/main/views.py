
from flask import render_template
from ..request import get_news
from app.main import app 


@app.route('/news/<int:id>')
def index(id):
    news = get_news(id)
    title = f'{news.title}'
  
    return render_template('index.html', title = title,news = news )