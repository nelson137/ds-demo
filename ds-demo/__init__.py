#!/var/www/ds-demo/ds-demo/venv/bin/python

from os.path import join
from time import time
from flask import Flask, url_for, render_template, redirect, request, flash
from pyrebase import initialize_app
from random import choice
from string import ascii_lowercase
from urllib.request import urlopen


app = Flask(__name__)
app.secret_key = '+J1OSR0e1qa5o2tdfxrAQqaR32cT7ipjSQI96wMVbfdRNTJgtSdlegii6x0PVzN7I+zc6MvV57s86V3vIn6kPg=='
app.url_map.strict_slashes = False

config = {
    'apiKey': 'AIzaSyDilfOiFc_Pe3lR8beDD2A64kLKG4pP_rQ',
    'authDomain': 'ds-demo-78281.firebaseapp.com',
    'databaseURL': 'https://ds-demo-78281.firebaseio.com',
    'projectId': 'ds-demo-78281',
    'storageBucket': 'ds-demo-78281.appspot.com',
    'serviceAccount': '/var/www/ds-demo/ds-demo/db-secret.json'
}

db = initialize_app(config).database()


@app.context_processor
def override_url_for():
    return dict(url_for=timestamped_url_for)


def timestamped_url_for(endpoint, **values):
    if endpoint == 'static':
        filename = values.get('filename', None)
        if filename:
            file_path = join(app.root_path, endpoint, filename)
            values['q'] = int(time())
    return url_for(endpoint, **values)


def create_entry(name, price, stars, ratings):
    db.push({
        'name': name,
        'price': price,
        'stars': stars,
        'ratings': ratings
    })


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/manual')
def form():
    return render_template('manual.html')


@app.route('/auto')
def auto():
    return render_template('auto.html')


@app.route('/form/submit', methods=['POST'])
def submit_form():
    # add ?next= arg to path for redirecting back to auto or manual
    name = request.form['name']
    price = request.form['price']
    stars = request.form['stars']
    ratings = request.form['ratings']
    create_entry(name, price, stars, ratings)

    flash('Form submitted successfully')
    return redirect('/manual')


@app.route('/scrape')
def scrape():
    return urlopen(request.args['url']).read()


if __name__ == '__main__':
    app.run(debug=True)
