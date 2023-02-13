from flask import Flask  # First we imported the Flask class

app = Flask(__name__)  # Next we create an instance of this class

@app.route('/')  # We then use the route() decorator to tell flask
                # Flask what URL should trigger our function
def hello_form():
    return "<h1><strong>Hello, this is a form!</strong></h1>"
    # This function returns the message we want to display in
    # In the users browser

#if __name__ == '__main__':
  #  app.run(debug=True)

# Python changes, terminate
# HTML, CSS changes, reload web page