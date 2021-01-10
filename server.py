from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/<first>/<second>')
def something(first, second):
    print(first, second)
    return 'ok'


app.run()
