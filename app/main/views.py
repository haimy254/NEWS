
from flask import render_template
from ..request import get_news
from app import app 
from request import get_news,get_news, search_news


@app.route('/news/<int:id>')
def index(id):
    news = get_news(id)
    title = f'{news.title}'
  
    return render_template('index.html', title = title,news = news )
@app.route('/search/<news_name>')
def search(news_name):
    news_name_list = news_name.split("")
    news_name_format = "+".join(news_name_list)
    searched_news= search_news(news_name_format)
    title = f'search results for {news_name}'
    return render_template('search.html',news= searched_news)