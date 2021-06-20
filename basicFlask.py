from typing import Protocol
from flask import Flask, render_template        #render_template accesses the html files and renders it

app = Flask(__name__)

@app.route('/')
def home():     #output this function produces is mapped to @app.route url
    return render_template("home.html")

@app.route('/about/')
def about():     #output this function produces is mapped to @app.route url
    return render_template("about.html")

@app.route('/justText/')
def jText():     #output this function produces is mapped to @app.route url
    return "Just some text here!"

if __name__ == "__main__":      #When script is executed "__name__" is assigned "__main__". When script is imported "__name__" is assigned "script1"
    app.run( debug = True )     #If script was imported this line is not executed
    

    
# on mac to find running ports
# sudo lsof -i :5000
# to kill the port 
# kill -9 <pid> 