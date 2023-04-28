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


@app.route('/', methods = ['GET','POST'])
def index():
    return render_template('index.html')


if __name__ == "__main__":
    app.run("localhost", 6969)