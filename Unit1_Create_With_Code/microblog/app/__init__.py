
from flask import Flask
from Unit1_Create_With_Code.microblog.config import Config

app = Flask(__name__)
app.config.from_object(Config)
app.config['SECRET_KEY'] = 'a very long string'

from Unit1_Create_With_Code.microblog.app import routes

