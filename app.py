# note the default port is 5000 FYI
import os
from flask import Flask

#testingCI

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World!"


@app.route('/<name>')
def hello_name(name):
    return "Hello {}!".format("name")

if __name__ == '__main__':
    app.run()
