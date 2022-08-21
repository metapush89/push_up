import random, os

content = f"""
import os
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

from flask import Flask
app = Flask(__name__)

@app.route('/trtst')
def trtst():
    FF_options = webdriver.FirefoxOptions()
    FF_profile = webdriver.FirefoxProfile()
    FF_options.add_argument("-headless")
	# enable trace level for debugging 
	FF_options.add_argument("-remote-debugging-port=9224")
	FF_options.add_argument("-headless")
	FF_options.add_argument("-disable-gpu")
	FF_options.add_argument("-no-sandbox")
    if 'DYNO' in os.environ:
        driver = webdriver.Firefox(executable_path=os.environ.get("GECKODRIVER_PATH"),firefox_binary=FirefoxBinary(os.environ.get("FIREFOX_BIN"))) 
    else:
        driver = webdriver.Firefox(options=FF_options, firefox_profile=FF_profile)
    driver.get("http://info.cern.ch/hypertext/WWW/TheProject.html")
    textResult = driver.execute_script('return document.querySelector("title").textContent')
    driver.close()
    textMatch = 'The World Wide Web project'
    return str(textResult == textMatch)

@app.route('/')
def index():
    return '<h1>Hello World! - {random.randint(1, 1000)}</h1>'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=os.environ.get('PORT', 5210))
"""

with open(os.path.join(os.getcwd(), 'server', 'app.py'), 'w') as f:
    f.write(content)
