import unittest
from model import news

News = news.News

class NewsTest(unittest.TestCases):
    def setUp(self):
        self.new_news = ('America goes down','John Wit','America goes to war with russia','bbc-news','http//bbc news.com')
        
    def test__init__(self):
        self.assertEqual(self.new_news.title,"America goes down")
        self.assertEqual(self.new_news.author,"John Wit")
        self.assertEqual(self.new_news.description,"America goes to war with russia")
        self.assertEqual(self.new_news.publishedAt,"bbd-news")
        self.assertEqual(self.new_news.image,"http//bbc news.com")
        
    def test_instance(self):
         self.assertTrue(isinstance(self.new_news,News))
         
if __name__=='__main__':
    unittest.main()   