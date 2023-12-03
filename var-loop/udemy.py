import random


huruf = ['a','A','b','B','c','C','d','D','e','E','f','F','g','G','h','H','i','I','j','J','k','K','l','L','m','M','n','N','o','O','p','P','q','Q','r','R','s','S','t','T','u','U','v','V','w','W','x','X','y','Y','z','Z']
nomor = ['1','2','3','4','5','6','7','8','9','0']
simbol = ['`','~','!','@','#','$','%','^','&','*','(',')','-','_','+','=','{','}','[',']',';',':','\',']

print(huruf[0])
password_list = []
a= int(0)

no_huruf = int(input("masukkan jumlah huruf"))
no_nomor = int(input("masukkan jumlah nomor")) 
no_simbol = int(input("masukkan jumlah simbol"))

for char in range(0,no_huruf):
    password_list.append(random.choice(huruf))


for char in range(0,no_nomor):
    password_list += random.choice(nomor)


for char in range(0,no_simbol):
    password_list += random.choice(simbol)

password =""

for char in password_list:
    # password += char memasukkan char(isi) password_list ke password
    # jika menggunakan sama dengan maka akan ganti setiap di loop 
    password += char

print(password)
