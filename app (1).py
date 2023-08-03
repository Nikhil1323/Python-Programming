from flask import Flask #flask is a python library that helps us to expose the python code to the 3rd 
                             # party software so that both can communicate.
from flask import request
app = Flask(__name__)
#here app is the object of the flask class.

@app.route("/")     # it is a decorator. "/" is the home route.
def hello_world():
    return "<h1>Hello, World!</h1>" #h1 is a tag in html which represents a header of size 1.

@app.route("/hello_world1")     # it is a decorator.
def hello_world1():
    return "<h2>Hello, World1!</h2>"

@app.route("/hello_world2")     # it is a decorator.
def hello_world2():
    return "<u><h3>Hello, World2!</h3></u>"

@app.route("/test")
def test():
    a = 5+6
    return "This is my function to print {}".format(a)

@app.route("/test2") # This function is called as url binding.
def test2():
    data = request.args.get("x")
    return "This is a data input from my url {}".format(data)

if __name__=="__main__":
    app.run(host="0.0.0.0")
