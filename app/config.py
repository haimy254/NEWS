import os
class Config:
    NEWS_API_BASE_URL='https://newsapi.org/v2/everything?q=Apple&from=2022-05-03&sortBy=popularity&apiKey=API_KEY'
    NEWS_API_KEY=os.environ.get('25a14688847949f39f86a855aa918ad8')
class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True
    
    
config_options = {
'development':DevConfig,
'production':ProdConfig
}