import unittest
class Source:
    '''
    Source class to define source Objects
    '''

    def __init__(self,id,name,description,url,category,country):
        self.id = id
        self.name = name
        self.description = description
        self.url =  url
        self.category = category
        self.country = country

class SourceTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Movie class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_source = Source("bbc-sport","BBC Sport","The home of BBC Sport online. Includes live sports coverage, breaking news, results, video, audio and analysis on Football, F1, Cricket, Rugby Union, Rugby League, Golf, Tennis and all the main world sports, plus major events such as the Olympic Games.","http://www.bbc.co.uk/sport ","sports","gb")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,Source))

if __name__ == '__main__':
    unittest.main()