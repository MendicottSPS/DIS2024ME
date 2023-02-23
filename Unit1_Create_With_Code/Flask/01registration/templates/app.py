from flask import Flask  # First we imported the Flask class
from registration import Registration
app = Flask(__name__)  # Next we create an instance of this class


@app.route('/')  # We then use the route() decorator to tell flask
# Flask what URL should trigger our function

def hello_form():
    return "<h1><strong>Hello, this is a form!</strong></h1>"
    # This function returns the message we want to display in the users browser


@app.route('/registration', methods=['GET', 'POST'])
def RegisterUser():
    form = Registration()
    if request.methods == 'POST':
        if form.validate() == False:
            return render_template('registration.html', form=form)
        else:
            return render_template('success.html')
    elif request.method == 'GET':
        return render_template('registration.html', form=form)


#if __name__ == '__main__':
 #   app.run(debug=True)

# Python changes, terminate and then run again
# HTML, CSS changes, reload web page
