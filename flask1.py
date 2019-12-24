from flask import Flask
app = Flask(__name__) 
# here name is name of module if __name__ == 'main'
#where flask can look for static files

# / is the root page of our website
# @route decorator will handle all of the complicated backend stuff
#
#    What is a route?
#   routes are what we type into browerser
#   to go to different pages
#   We use decorator for that.

#decorator to add some additional functionalities to existing functions
@app.route("/")
@app.route("/home")
#multiple routes handling the same function
def hello():
    return "<h1>Hello World!</h1>"
@app.route("/about")
def about():
    return "<h1>I really like FLASK</h1>"
if __name__ == '__main__':
    app.run(debug=True)


# 127.0.0.1 replace that with local host