nama = input("siapa nama ? ")
#harus satu baris if elsenya 
#kondisi tidak perlu tanda kurung

if nama=="abi" : 
    print("Muhammad Haris Maualana Koliq Abiansyah")
    print(f"ini {nama}")
    print("belajar python")

#tidak ada else if adanya elif
elif nama=="haris":
    print("hello world")
else : 
    print(f"kamu {nama}")

kangka=[9,1,2,3,4]

for i in kangka :
    print(f"i sekarang => {i} = {kangka}")

print("end program")

# contoh while 
a = 0


while a<4 :
    a+=1
    print("angka sekarang " , a)
    if a == 4 :
        print("nice")
        #continue untuk menstop sementara while dengan kondisinya dan hasil continue mengembalikan ke while lagi
        continue
    # harus dikasih counter
    # += itu menambahkan pada variablenya sendiri
    print("ini")
    
a = 0
while a<6 :
    a+=1
    print("angka sekarang " , a)
    if a == 4 :
        print("nice")
        #break untuk menghentikan while
        break
    # harus dikasih counter
    # += itu menambahkan pada variablenya sendiri
    print("hello")
    


else : 
    print(f"kamu {nama}")