from .models import News
# from app import app
import urllib.request,json
# from .model import news

api_key = None
base_url = None
def configure_request(app):
  global_api_key,base_url
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
      title= News.item.get('original_title')
      author = News.item.get('author')
      description= news_item.get('description')
      publishedAt=News.item.get('publishedAt')
      image=News.items.get('image')
      
      if News:
        news_object= News(title,author,description,publishedAt, image)
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
      

def search_news(news_name):
  search_news_url ='https://newsapi.org/v2/everything?q=Apple&from=2022-05-03&sortBy=popularity&apiKey=API_KEY'.format (api_key, news_name)
  with urllib.request.urlopen(search_news_url) as url:
   search_news_data = url.read()
  search_news_response = json.loads(search_news_data)
  search_news_results = None
  if search_news_response['results']:
    search_news_list = search_news_response['results']
    search_news_results = process_results(search_news_list)


    return search_news_results
    