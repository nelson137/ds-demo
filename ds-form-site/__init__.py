#!/var/www/ds-form-site/ds-form-site/venv/bin/python

import os
from flask import Flask, url_for, render_template, request

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
    pass

if __name__ == '__main__':
    app.run(debug=True)

