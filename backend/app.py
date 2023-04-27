from flask import Flask,request,render_template
import flask
import json
from flask_cors import CORS
import mysql.connector as sqltor
# app = Flask(__name__)
# CORS(app)

# @app.route("/")
# def hello():
#     return "Hello, World!"

# @app.route('/users', methods=["GET"])
# def users():
#     print("users endpoint reached...")
#     with open("users.json", "r") as f:
#         data = json.load(f)
#         data.append({
#             "username": "user4",
#             "pets": ["hamster"]
#         })

#         return flask.jsonify(data)


app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/index2', methods = ['GET','POST'])
def index2():
    if(request=='POST'):
        mycon = sqltor.connect(
        host = 'localhost',
        user = 'root',
        password = 'root')
        mycursor = mycon.cursor()
        mycursor.execute("USE SMP_Pet_Shop;")
        mycursor.execute(f"SELECT * FROM DOGS WHERE breed = '{Labrador}';")
        data = mycursor.fetchall()
        return data
    return render_template('index2.html')


if __name__ == "__main__":
    app.run("localhost", 6969)