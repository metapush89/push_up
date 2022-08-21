import random, os

content = f"""
import os
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

from flask import Flask
from flask_autoindex import AutoIndex

app = Flask(__name__)
files_index = AutoIndex(app, browse_root="/", add_url_rules=False)

@app.route('/rootdir')
@app.route('/rootdir/<path:path>')
def autoindex(path='.'):
    return files_index.render_autoindex(path)

@app.route('/currdir')
@app.route('/currdir/<path:path>')
def autoindex2(path=os.getcwd()):
    return files_index.render_autoindex(path)

@app.route('/')
def index():
    return '<h1>Hello World! - {random.randint(1, 1000)}</h1>'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=os.environ.get('PORT', 5210))
"""

with open(os.path.join(os.getcwd(), 'server', 'app.py'), 'w') as f:
    f.write(content)
