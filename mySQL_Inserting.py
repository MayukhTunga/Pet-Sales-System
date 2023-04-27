import mySQL_Creation as create
import dog as Doggo
import cat as Kitty
import AvailableDogs as availDog
import AvailableCats as availCat
import mysql.connector as sqltor

lab1 = Doggo.Dog()
lab2 = Doggo.Dog()
lab3 = Doggo.Dog()
availDog.labrador(lab1,lab2,lab3)

husky1 = Doggo.Dog()
husky2 = Doggo.Dog()
husky3 = Doggo.Dog()
availDog.husky(husky1,husky2,husky3)

gShep1 = Doggo.Dog()
gShep2 = Doggo.Dog()
gShep3 = Doggo.Dog()
availDog.germanShepherd(gShep1,gShep2,gShep3)


siamCat1 = Kitty.Cat()
siamCat2 = Kitty.Cat()
siamCat3 = Kitty.Cat()
availCat.siameseCat(siamCat1, siamCat2, siamCat3)

persCat1 = Kitty.Cat()
persCat2 = Kitty.Cat()
persCat3 = Kitty.Cat()
availCat.persianCat(persCat1, persCat2, persCat3)

britsCat1 = Kitty.Cat()
britsCat2 = Kitty.Cat()
britsCat3 = Kitty.Cat()
availCat.britishShortHair(britsCat1, britsCat2, britsCat3)


create.connection()

mycon = sqltor.connect(
    host = 'localhost',
    user = 'root',
    password = 'root')

mycursor = mycon.cursor()


mycursor.execute("USE SMP_Pet_Shop;")

#name, gender, dob, age, height, weight, breed, trained, affectionate
insertDoggoTable = f"""INSERT INTO Dogs 
VALUES(1, '{lab1.name}', '{lab1.gender}', '{lab1.dob}', {lab1.age}, {lab1.height}, {lab1.weight}, '{lab1.breed}', '{lab1.trained}', '{lab1.affectionate}'),
(2, '{lab2.name}', '{lab2.gender}', '{lab2.dob}', {lab2.age}, {lab2.height}, {lab2.weight}, '{lab2.breed}', '{lab2.trained}', '{lab2.affectionate}'),
(3, '{lab3.name}', '{lab3.gender}', '{lab3.dob}', {lab3.age}, {lab3.height}, {lab3.weight}, '{lab3.breed}', '{lab3.trained}', '{lab3.affectionate}'),
(4, '{husky1.name}', '{husky1.gender}', '{husky1.dob}', {husky1.age}, {husky1.height}, {husky1.weight}, '{husky1.breed}', '{husky1.trained}', '{husky1.affectionate}'),
(5, '{husky2.name}', '{husky2.gender}', '{husky2.dob}', {husky2.age}, {husky2.height}, {husky2.weight}, '{husky2.breed}', '{husky2.trained}', '{husky2.affectionate}'),
(6, '{husky3.name}', '{husky3.gender}', '{husky3.dob}', {husky3.age}, {husky3.height}, {husky3.weight}, '{husky3.breed}', '{husky3.trained}', '{husky3.affectionate}'),
(7, '{gShep1.name}', '{gShep1.gender}', '{gShep1.dob}', {gShep1.age}, {gShep1.height}, {gShep1.weight}, '{gShep1.breed}', '{gShep1.trained}', '{gShep1.affectionate}'),
(8, '{gShep2.name}', '{gShep2.gender}', '{gShep2.dob}', {gShep2.age}, {gShep2.height}, {gShep2.weight}, '{gShep2.breed}', '{gShep2.trained}', '{gShep2.affectionate}'),
(9, '{gShep3.name}', '{gShep3.gender}', '{gShep3.dob}', {gShep3.age}, {gShep3.height}, {gShep3.weight}, '{gShep3.breed}', '{gShep3.trained}', '{gShep3.affectionate}');
"""

insertKittyTable = f"""INSERT INTO Cats 
VALUES(1, '{siamCat1.name}', '{siamCat1.gender}', '{siamCat1.dob}', {siamCat1.age}, {siamCat1.height}, {siamCat1.weight}, '{siamCat1.breed}', '{siamCat1.friendly}', '{siamCat1.responds}'),
(2, '{siamCat2.name}', '{siamCat2.gender}', '{siamCat2.dob}', {siamCat2.age}, {siamCat2.height}, {siamCat2.weight}, '{siamCat2.breed}', '{siamCat2.friendly}', '{siamCat2.responds}'),
(3, '{siamCat3.name}', '{siamCat3.gender}', '{siamCat3.dob}', {siamCat3.age}, {siamCat3.height}, {siamCat3.weight}, '{siamCat3.breed}', '{siamCat3.friendly}', '{siamCat3.responds}'),
(4, '{persCat1.name}', '{persCat1.gender}', '{persCat1.dob}', {persCat1.age}, {persCat1.height}, {persCat1.weight}, '{persCat1.breed}', '{persCat1.friendly}', '{persCat1.responds}'),
(5, '{persCat2.name}', '{persCat2.gender}', '{persCat2.dob}', {persCat2.age}, {persCat2.height}, {persCat2.weight}, '{persCat2.breed}', '{persCat2.friendly}', '{persCat2.responds}'),
(6, '{persCat3.name}', '{persCat3.gender}', '{persCat3.dob}', {persCat3.age}, {persCat3.height}, {persCat3.weight}, '{persCat3.breed}', '{persCat3.friendly}', '{persCat3.responds}'),
(7, '{britsCat1.name}', '{britsCat1.gender}', '{britsCat1.dob}', {britsCat1.age}, {britsCat1.height}, {britsCat1.weight}, '{britsCat1.breed}', '{britsCat1.friendly}', '{britsCat1.responds}'),
(8, '{britsCat2.name}', '{britsCat2.gender}', '{britsCat2.dob}', {britsCat2.age}, {britsCat2.height}, {britsCat2.weight}, '{britsCat2.breed}', '{britsCat2.friendly}', '{britsCat2.responds}'),
(9, '{britsCat3.name}', '{britsCat3.gender}', '{britsCat3.dob}', {britsCat3.age}, {britsCat3.height}, {britsCat3.weight}, '{britsCat3.breed}', '{britsCat3.friendly}', '{britsCat3.responds}');
"""

mycursor.execute(insertDoggoTable)
mycursor.execute(insertKittyTable)
mycon.commit()

# mycursor.execute("SELECT JSON_ARRAYAGG(json_object('name',name,'breed',breed)) FROM DOGS;")
# data = mycursor.fetchall(
# print(type(data))
# print(data)