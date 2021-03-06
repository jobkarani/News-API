from flask import render_template,request,redirect,url_for
from . import main
from ..request import get_source,get_article


@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    # Getting popular movie
    popular_sources = get_source()
    # print("sources" ,popular_sources)
    business_news = get_source()
    sport_news = get_source()
    

    title = 'Home - Welcome to Online News Website'
    return render_template('index.html', title = title, popular = popular_sources,business = business_news,sport = sport_news )

@main.route('/articles/<source_id>')
def articles(source_id):
    articles = get_article(source_id)
    print(articles)

    return render_template('articles.html',articles = articles)

    


