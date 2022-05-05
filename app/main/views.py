
from turtle import title
from flask import render_template
from ..request import get_news
from app import app 
from request import get_news,get_news, search_news
from flask import render_template,request,redirect,url_for



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

@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    # Getting popular movie
    business_news = get_news('business')
    entertainment_news= get_news('entertainment')
    general_news = get_news('general')
    
    title = 'News headlines'
    search_news = request.args.get('news_query')

    if search_news:
        return redirect(url_for('search',movie_name=search_news))
    else:
        return render_template('index.html', title = title, business =  business_news, entertainment  = entertainment_news, general =  general_news )