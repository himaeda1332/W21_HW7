#########################################
##### Name: Hisamitsu Maeda         #####
##### Uniqname: himaeda             #####
#########################################

from flask import Flask, render_template
import requests

import secrets

app = Flask(__name__)
API_KEY = secrets.api_key
BASE_URL = "https://api.nytimes.com/svc/topstories/v2/technology.json"
params = {"api-key": API_KEY}

@app.route('/')
def index():
    return '<h1>Welcome!</h1>'

@app.route('/name/<name>')
def name(name):
    return render_template('name.html',
        name=name)

@app.route('/headlines/<name>')
def show_headlines(name):
    response = requests.get(BASE_URL, params).json()
    headlines = []
    for story in response['results'][:5]:
        headlines.append(story['title'])
    return render_template('headlines.html',
                            name=name,
                            headlines=headlines)

@app.route('/links/<name>')
def show_headlines_with_link(name):
    response = requests.get(BASE_URL, params).json()
    headline_links = []
    for story in response['results'][:5]:
        headline_links.append((story['title'], story['url']))
    return render_template('links.html',
                            name=name,
                            headline_links=headline_links)

@app.route('/images/<name>')
def show_headlines_with_link_and_thumbnail(name):
    response = requests.get(BASE_URL, params).json()
    headline_link_thumbnails = []
    for story in response['results'][:5]:
        headline_link_thumbnails.append((story['title'],
                                        story['url'],
                                        story['multimedia'][0]['url']))
    return render_template('images.html',
                            name=name,
                            headline_link_thumbnails=headline_link_thumbnails)

if __name__ == '__main__':
    app.run(debug=True)