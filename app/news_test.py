import unittest
from model import news

News = news.News

class NewsTest(unittest.TestCases):
    def setUp(self):
        self.new_news = ('America goes down','John Wit','America goes to war with rassia','bbc-news','http//bbc news.com')
        
    def test_instance(self):
         self.assertTrue(isinstance(self.new_news,News))
         
if __name__=='__main__':
    unittest.main()   