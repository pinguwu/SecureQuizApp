import os
from flask import Flask, url_for, render_template, request
from flask import redirect
from flask import session

app = Flask(__name__)


app.secret_key=os.environ["SECRET_KEY"];



@app.route("/")
def render_main:
    return render_template('home.html')

@app.route('/page1')
def renderPage1:
    return render_template('page1.html')
