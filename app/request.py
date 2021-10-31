from app import app
import urllib.request,json
from .models import movie

Source = source.Source
# Getting api key
api_key = app.config['MOVIE_API_KEY']