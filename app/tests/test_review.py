import unittest
from app.models import News, Review

class ReviewTest(unittest.TestCase):
    def setUp(self):
        self.new_review= Review(000,'America','','ratings')
        
    def test_instance(self):
        self.assertTrue(isinstance(self.new_news,News))