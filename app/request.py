
from app.main import app
import urllib.request,json
from .model import news

News = news.News
api_key= app.config['NEWS_API_KEY']
base_url = app.config['NEWS_API_BASE_URL']

def get_news(category):
  get_news_url = base_url.format(category,api_key)

  with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None
        if get_news_response['results']:
           news_results_list = get_news_response['results']
           news_results = process_results(news_results_list)
           
def process_results(news_list):
    news_results = []
    for news_item in news_list:
      title= news.item.get('original_title')
      author = news.item.get('author')
      description= news_item.get('description')
      publishedAt=news.item.get('publishedAt')
      image=news.items.get('image')
      
      if news:
        news_object= news(title,author,description,publishedAt, image)
        news_results.append(news_object)
       
        return news_results

def get_news(id):
  get_news_details_url = base_url.format(id,api_key)
  with urllib.request.urlopen(get_news_details_url) as url:
    news_details_data = url.read()
    news_details_response = json.loads(news_details_data)
    
    news_object = None
    if news_details_response:
      title= news_details_response.get('title')
      author= news_details_response.get('author')
      description= news_details_response.get('description')
      publishedAt= news_details_response.get('publishedAt')
      image= news_details_response.get('image')
      
      news_object = News(title,author, description,publishedAt,image)
      
      return news_object