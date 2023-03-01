from app import app
from flask import render_template, flash, redirect, url_for

from Unit1_Create_With_Code.microblog.app.forms import LoginForm


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
            'author': {'username': 'Mollie'},
            'body': 'Mondays are the worst!'
        }
    ]
    return render_template('index.html', title=user['username'], user=user, posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)

