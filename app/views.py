from flask import render_template
from app import app
from .request import get_source

@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    # Getting popular movie
    popular_sources = get_source()
    print("sources" ,popular_sources)
    title = 'Home - Welcome to Online News Website'
    return render_template('index.html', title = title, popular = popular_sources)