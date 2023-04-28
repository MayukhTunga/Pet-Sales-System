import mysql.connector as sqltor
def connection():
    mycon = sqltor.connect(
        host = 'localhost',
        user = 'root',
        password = 'root')

    mycursor = mycon.cursor()
    mycursor.execute("DROP DATABASE IF EXISTS SMP_PET_SHOP;")
    mycursor.execute("CREATE DATABASE IF NOT EXISTS SMP_Pet_Shop;")
    mycursor.execute("USE SMP_Pet_Shop;")

    #name, gender, dob, age, height, weight, breed, trained, affectionate
    createTableDoggo = """CREATE TABLE IF NOT EXISTS Dogs(
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
    mycursor.execute(createTableDoggo)
    mycon.commit()

    #name, gender, dob, age, height, weight, breed, friendly, responds
    createTableCat = """CREATE TABLE IF NOT EXISTS Cats(
        SerialNo INT PRIMARY KEY,
        Name VARCHAR(50),
        Gender CHAR,
        DOB DATE,
        AGE INT,
        Height INT,
        Weight INT,
        Breed VARCHAR(50),
        Friendly VARCHAR(6),
        Responds VARCHAR(6)
    );"""
    mycursor.execute(createTableCat)
    mycon.commit()


