#!/var/www/ds-form-site/ds-form-site/venv/bin/python

import gspread, random
from os.path import join, dirname
from time import time
from flask import Flask, url_for, render_template, redirect, request, flash
from string import ascii_lowercase
from oauth2client.service_account import ServiceAccountCredentials


app = Flask(__name__)
app.secret_key = '+J1OSR0e1qa5o2tdfxrAQqaR32cT7ipjSQI96wMVbfdRNTJgtSdlegii6x0PVzN7I+zc6MvV57s86V3vIn6kPg=='


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


@app.route('/')
def form():
    return render_template('form.html')


@app.route('/submit_form', methods=['GET', 'POST'])
def submit_form():
    '''scope = ['https://spreadsheets.google.com/feeds']
    creds = ServiceAccountCredentials.from_json_keyfile_name(join(dirname(__file__), 'client_secret.json'), scope)
    client = gspread.authorize(creds)

    sheet = client.open('Demo DB').sheet1

    row_count = len(sheet.get_all_values())
    sheet.insert_row([row_count, random.choice(ascii_lowercase)*5], row_count+1)'''

    flash('Form submitted successfully')

    return redirect(url_for('form'))


if __name__ == '__main__':
    app.run(debug=True)
