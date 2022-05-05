
# from turtle import title
# from flask import render_template
# from ..request import get_news
# from app import app 
from request import get_news,get_news, search_news
from flask import render_template,request,redirect,url_for
from .. import main
from ..main import review
from .forms import ReviewForm
Review = review.Review




@main.route('/news/<int:id>')
def index(id):
    news = get_news(id)
    title = f'{news.title}'
  
    return render_template('index.html', title = title,news = news )
@main.route('/search/<news_name>')
def search(news_name):
    news_name_list = news_name.split("")
    news_name_format = "+".join(news_name_list)
    searched_news= search_news(news_name_format)
    title = f'search results for {news_name}'
    return render_template('search.html',news= searched_news)

@main.route('/')
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
    
@main.route('/news/review/new/<int:id>', methods = ['GET','POST'])
def new_review(id):
    form = ReviewForm()
    news = get_news(id)
    
    if form.validate_on_submit():
        title = form.title.data
        review = form.review.data
        new_review = Review(news.id,title,news.poster,review)
        new_review.save_review()
        return redirect(url_for('news',id = news.id ))
    title = f'{news.title} review'
    return render_template('new_review.html',title = title, review_form=form, news=news)
@main.route('/news/<int:id')
def news(id):
    news = get_news(id)
    title = f'{news.title}'
    reviews = Review.get_reviews(news.id)
    return render_template('news.html',title = title,news = news,reviews = review)