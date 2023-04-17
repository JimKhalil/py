#output
print("hello world")

# ini comment
"""multi line comment"""

#variabel
a = 10 
print(a)

#cara mengcompile buka terminal dan mengcompile
#python -m py_compile text.py
#variable
# seperti js jadi nilai a yang terbaru itu yang di deklarasi
a = 15
x = 5
print("ini nilai a =",a)

#tipe data
# tipe data integer 
data_integer = 11
print("data :", data_integer)
print("- bertipe : ", type(data_integer))
# tipe data float bisa titik atau koma untuk desimal
data_float = 0.1
print("data :",data_float)
print("- bertipe : ", type(data_float))
# tipe data string 
data_string = "ucup"
print("data :",data_string)
print("- bertipe : ", type(data_string))
#tipe data boolean
data_bool =  False
print("data :",data_bool)
print("- bertipe : ", type(data_bool))
#bilangan kompleks
data_complex = complex(5,6)
print("data :", data_complex)
print("- bertipe : ", type(data_complex))

#casting data atau merubah tipe data
#tipe data = int, str, float, int
data_int = 9
data_float = float(data_int)
data_str = str(data_int)
data_bool = bool(data_int)

"""
untuk ketentuan
str => int/float harus angka
str => int/float tidak boleh null 
str = null => bool false
"""
print(data_int,"=", type(data_int))
print(data_float,"=", type(data_float))
print(data_str,"=", type(data_str))
print(data_bool, "=", type(data_bool))

#input dari user
#input data pasti string
data = input("masukkan data")
print (data, type(data))
#untuk merubah input dengan casting data
data_int = int(input("masukkan int"))
print (data_int, type(data_int))