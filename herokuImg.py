import random, os

content = f"""
# Generate a basic flask application
import os
from flask import Flask
app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Hello World! - {random.randint(1, 1000)}</h1>'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=os.environ.get('PORT', 5210))

"""

with open(os.path.join(os.getcwd(), 'server', 'app.py'), 'w') as f:
    f.write(content)