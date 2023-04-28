from flask import Flask,request,render_template
from flask_mysqldb import MySQL
import json
from flask_cors import CORS
import mysql.connector as sqltor
import pandas as pd

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'SMP_PET_SHOP'

mysql = MySQL(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/Labrador')
def index6():
    return render_template('/../frontend/Labrador.html')

@app.route('/../frontend/Husky')
def index1():
    return render_template('Husky.html')

@app.route('/German Shepherd')
def index2():
    return render_template('/../frontend/German Shepherd.html')

@app.route('/Siamese Cat')
def index3():
    return render_template('/../frontend/Siamese Cat.html')

@app.route('/Persian Cat')
def index4():
    return render_template('/../frontend/Persian Cat.html')

@app.route('/British Short Hair')
def index5():
    return render_template('/../frontend/British Short Hair.html')

if __name__ == "__main__":
    app.run("localhost", 6969)