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
a = 1

while a<6 :
    print(a)
    # harus dikasih counter
    # += itu menambahkan pada variablenya sendiri
    a+=1
