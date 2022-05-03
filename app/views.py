from flask import render_template
from .request import get_news
from app import app 

@app.route('/')
def index():
    
    business_news= get_news('business')
    print(business_news)
    title = 'home - Welcome to current world wide news website online'
    
    business_news= get_news('business')
    entertainment_news= get_news('entertainment')
    general_news= get_news('general')
    health_news= get_news('health')
    science_news=get_news('science')
    technology_news= get_news('technology')
    sport_news= get_news('sport')
    return render_template('index.html', title = title,business = business_news, entertainment= entertainment_news, general= general_news, health = health_news, science= science_news, technology = technology_news, sport= sport_news)