from app import app

@app.route('/')
@app.route('/index')
def index():
    return "<h1>Hello, Everyone in Year 11 Digital Solutions!</h1>"

