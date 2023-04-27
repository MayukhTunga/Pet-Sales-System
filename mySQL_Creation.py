import mysql.connector as sqltor
import AvailableDogs as doggo
import AvailableCats as kitty
from dog import *
from cat import *
from bird import *


mycon = sqltor.connect(
    host = 'localhost',
    user = 'root',
    password = 'root')

mycursor = mycon.cursor()

mycursor("CREATE DATABASE IF NOT EXISTS SMP_Pet_Shop;")
mycursor("USE SMP_Pet_Shop;")

#name, gender, dob, age, height, weight, breed, trained, affectionate
createTableDoggo = """CREATE TABLE Dogs(
    SerialNo INT PRIMARY KEY,
    Name VARCHAR(50),
    Gender CHAR,
    DOB DATE,
    AGE INT,
    Height INT,
    Weight INT,
    Breed VARCHAR(50),
    Trained VARCHAR(6),
    Affectionate VARCHAR(6)
);"""
cursor.execute(createTableDoggo)

