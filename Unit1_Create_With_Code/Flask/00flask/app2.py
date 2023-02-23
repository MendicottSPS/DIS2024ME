# app2.py
from flask import Flask, render_template, request
#  from registration import Registration

app = Flask(__name__)
app.config['SECRET_KEY'] = 'a very long string'

@app.route('/')
def hello_form():
    return '<H1>Hello, Form!</H1>'

if __name__ == '__main__':
    app.run(debug=True)

