class Source:
    '''
    Source class to define source Objects
    '''

    def __init__(self,author,title,description,url,urlToImage,publishDate):
        self.author =author
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.publishDate = publishDate