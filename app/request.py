from app import app
import urllib.request,json
from .models import source
from .articles import Article




Source = source.Source
# Getting api key
api_key = app.config['NEWS_API_KEY']

# Getting the movie base url
base_url = app.config["NEWS_API_BASE_URL"]

def get_source():
    '''
    Function that gets the json response to our url request
    '''
    source_url = 'https://newsapi.org/v2/sources?apiKey=36909ae7e31543ddaf8bb4141dc92252'
    print(source_url)

    with urllib.request.urlopen(source_url) as url:
        get_source_data = url.read()
        get_source_response = json.loads(get_source_data)

        source_results = None

        if get_source_response['sources']:
            source_results_list = get_source_response['sources']
            source_results = process_results(source_results_list)

    return source_results

def process_results(source_result):
    '''
    Function that processes the source list result and transform them to a list of Objects
    '''
    source_results = []
    for one_result in source_result:
        id = one_result.get('id')
        name = one_result.get('name')
        description = one_result.get('description')
        url = one_result.get('url')
        category = one_result.get('category')
        language = one_result.get('language')

        source_object = Source(id, name, description, url, category, language)
        source_results.append(source_object)

    return source_results

def process_articles_results(articles_result):
    articles_results = []
    for one_result in articles_result:
        author = one_result.get('author')
        title = one_result.get('title')
        description = one_result.get('description')
        url = one_result.get('url')
        urlToImage = one_result.get('urlToImage')
        publishedAt = one_result.get('publishedAt')
        content = one_result.get('content')

        article_object = Article(author,title, description, url, urlToImage, publishedAt,content)
        articles_results.append(article_object)

    return articles_results

def get_article(source_id):

    source_url = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey=36909ae7e31543ddaf8bb4141dc92252'.format(source_id)
    print(source_url)

    with urllib.request.urlopen(source_url) as url:
        get_source_data = url.read()
        get_source_response = json.loads(get_source_data)

        source_results = None

        if get_source_response['articles']:
            source_results_list = get_source_response['articles']
            source_results = process_articles_results(source_results_list)

    return source_results
