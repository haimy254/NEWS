class News:
    '''
    News class to define Movie Objects
    '''

    def __init__(self,title,author,image,description,publishedAt):
        self.title = title
        self.author = author
        self.image = "https://s.yimg.com/os/creatr-uploaded-images/2021-12/b4c77e50-5e45-11ec-97eb-d4c0e86e5f90" + image
        self.description = description
        self.publishedAt = publishedAt



class Review:

    all_reviews = []

    def __init__(self,news_id,title,imageurl,review):
        self.news_id = news_id
        self.title = title
        self.imageurl = imageurl
        self.review = review


    def save_review(self):
        Review.all_reviews.append(self)


    @classmethod
    def clear_reviews(cls):
        Review.all_reviews.clear()

    @classmethod
    def get_reviews(cls,id):

        response = []

        for review in cls.all_reviews:
            if review.news_id == id:
                response.append(review)

        return response
