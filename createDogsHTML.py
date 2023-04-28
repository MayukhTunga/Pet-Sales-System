import pandas as pd
import mysql.connector as sqltor
from IPython.display import HTML

mycon = sqltor.connect(
    host = 'localhost',
    user = 'root',
    password = 'root')

mycursor = mycon.cursor()
mycursor.execute("USE SMP_Pet_Shop;")

def createHTMLDoggo(breed):
    mycursor.execute(f"SELECT * FROM DOGS WHERE BREED LIKE '{breed}%';")
    data = mycursor.fetchall()
    col = ['Serial No.','Name','Gender','DOB','Age','Height','Weight','Breed','Trained?','Affectionate?']
    dat = []
    for x in data:
        dat.append(x)
    df = pd.DataFrame(dat,columns = col)
    df.to_html(f'frontend/{breed}.html')


def createHTMLKitty(breed):
    mycursor.execute(f"SELECT * FROM CATS WHERE BREED LIKE '{breed}%';")
    data = mycursor.fetchall()
    col = ['Serial No.','Name','Gender','DOB','Age','Height','Weight','Breed','Friendly','Responds To Name?']
    dat = []
    for x in data:
        dat.append(x)
    df = pd.DataFrame(dat,columns = col)
    df.to_html(f'frontend/{breed}.html',classes='table table-stripped')    

doggoBreeds = ['Labrador', 'Husky', 'German']
kittyBreed = ['Siamese', 'Persian', 'British']

for i in doggoBreeds:
    createHTMLDoggo(i)

for i in kittyBreed:
    createHTMLKitty(i)
