from flask import Flask
app=Flask(__name__)


@app.route('/hello')
def hello():
    return "Hello World!"

@app.route('/')
def hi():
    return "Hi World!"

@app.route('/greet')
def greet():
    return "Welcome Omkar"

@app.route('/wish')
def wish():
    return "Welcome Sandeep"

@app.route('/trip')
def trip():
    return "Welcome to Karma Experiences"

@app.route('/place')
def place():
    return "Welcome to Goa"

@app.route('/falls')
def falls():
    return "Welcome to Doodhsagar"

@app.route('/guest')
def Guest():
    return "Welcome to Nithin sir"

@app.route('/cost')
def cost():
    return "Cost is 2999"



if __name__ == "__main__":
    app.run(host="0.0.0.0.",debug=False)
