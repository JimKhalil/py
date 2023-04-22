import datetime as dt

#format string

#dapat menggunakan angka bilangan bulat

"""
:, untuk , di ordo bilangan ribuan
:3f untuk mengambil 3 angka float dibelakang  koma 
:d bilangan bulat
:% untuk jadi persen
:%2 untuk mengambil berapa angka di belakang titik
"""
nama = "abi"
format_str = (f"muhammad haris maulana koliq {nama}")
print(format_str)

#operasi aritmatika didalam format string

a=10000
b=2

format_str = (f"nilai {a*b:,}")

print(format_str)

#harus import untuk menggunakan fungsi date

#kenapa jadi dt karena datetime diganti menjadi variable dt

hari_ini = dt.date.today()

print(hari_ini)

print(f"hello {hari_ini:%A}")

tanggal = dt.date(2005,10,10)

print(tanggal)