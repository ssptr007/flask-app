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
    return "Hi Good morning have a nice day!"

@app.route('/varada')
def Varada():
    return "Varada dummy"





if __name__ == "__main__":
    app.run(host="0.0.0.0.",debug=False)
