import unittest
from model import news

News = news.News

class NewsTest(unittest.TestCases):
    def setUp(self):
        self.new_news = ('America goes down','John Wit','America goes to war with russia','bbc-news',"https://s.yimg.com/os/creatr-uploaded-images/2021-12/b4c77e50-5e45-11ec-97eb-d4c0e86e5f90")
        
    # def test__init__(self):
    #     self.assertEqual(self.new_news.title,"America goes down")
    #     self.assertEqual(self.new_news.author,"John Wit")
    #     self.assertEqual(self.new_news.description,"America goes to war with russia")
    #     self.assertEqual(self.new_news.publishedAt,"bbd-news")
    #     self.assertEqual(self.new_news.image,"https://s.yimg.com/os/creatr-uploaded-images/2021-12/b4c77e50-5e45-11ec-97eb-d4c0e86e5f90")
        
    def test_instance(self):
         self.assertTrue(isinstance(self.new_news,News))
         
if __name__=='__main__':
    unittest.main()   