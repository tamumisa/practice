import os,geocoder,json
from flask import Flask,render_template,url_for,flash,redirect,request
import sqlite3
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import distinct

app = Flask(__name__)

@app.route("/")
def index():
	return render_template('/top.html')

@app.route('/top',methods=["POST"])
def top():
	return render_template('/main.html')

@app.route('/upload')
def upload():
	return render_template('/upload.html')

if __name__ == "__main__":
	app.debug = True
	app.run(port=7000)

