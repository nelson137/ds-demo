#!/var/www/ds-form-site/ds-form-site/venv/bin/python

import os, gspread, random
from flask import Flask, url_for, render_template, request
from string import ascii_lowercase
from oauth2client.service_account import ServiceAccountCredentials


app = Flask(__name__)


@app.context_processor
def override_url_for():
    return dict(url_for=timestamped_url_for)

def timestamped_url_for(endpoint, **values):
    if endpoint == 'static':
        filename = values.get('filename', None)
        if filename:
            file_path = os.path.join(app.root_path, endpoint, filename)
            values['q'] = int(os.stat(file_path).st_mtime)
    return url_for(endpoint, **values)


@app.route('/')
def form():
    return render_template('form.html')


@app.route('/submit_form', methods=['POST'])
def submit_form():
    with open(os.path.join(os.path.dirname(__file__), 'submit_form.txt'), 'a') as f:
        f.write('submit %d' % len(f.readlines()))

    scope = ['https://spreadsheets.google.com/feeds']
    creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
    client = gspread.authorize(creds)

    sheet = client.open('Demo DB').sheet1

    row_count = len(sheet.get_all_values())
    sheet.insert_row([row_count, random.choice(ascii_lowercase)*5], row_count+1)


if __name__ == '__main__':
    app.run(debug=True)
