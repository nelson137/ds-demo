#!/var/www/ds-demo/ds-demo/venv/bin/python

from os.path import join
from time import time
from flask import Flask, url_for, render_template, redirect, request, flash
from pyrebase import initialize_app
from random import choice
from string import ascii_lowercase


app = Flask(__name__)
app.secret_key = '+J1OSR0e1qa5o2tdfxrAQqaR32cT7ipjSQI96wMVbfdRNTJgtSdlegii6x0PVzN7I+zc6MvV57s86V3vIn6kPg=='

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


@app.route('/form')
def form():
    return render_template('form.html')


def create_entry(name, price, stars, ratings):
    entry = {
        'name': name,
        'price': price,
        'stars': stars,
        'ratings': ratings
    }
    db.push(entry)


@app.route('/form/submit', methods=['GET', 'POST'])
def submit_form():
    name = request.form['name']
    price = request.form['price']
    stars = request.form['stars']
    ratings = request.form['ratings']
    create_entry(name, price, stars, ratings)

    flash('Form submitted successfully')
    return redirect('/form')


if __name__ == '__main__':
    app.run(debug=True)

