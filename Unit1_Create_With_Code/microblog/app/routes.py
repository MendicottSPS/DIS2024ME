from app import app
from flask import render_template


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Mollie'}
    posts = [
        {
            'author': {'username': 'Fred'},
            'body': 'Beautiful day in Brisbane!'
        },
        {
            'author': {'username': 'Wilma'},
            'body': 'Basketball is the best sport!'
        },
        {
            'author': {'username': 'Hannah'},
            'body': 'Mondays are the worst!'
        }
    ]
    return render_template('index.html', title=user['username'], user=user, posts=posts)

