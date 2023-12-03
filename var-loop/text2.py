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

"""
format angka lain 

bilangan bulat => binary bin() 
bilangan bulat => octal oct()
bilangan bulat => hexadecimal hex()

ini dapat dimasukkan ke format string
"""

#harus import datetime untuk menggunakan fungsi date

#kenapa jadi dt karena datetime diganti menjadi variable dt

hari_ini = dt.date.today()

print(hari_ini)

print(f"hello {hari_ini:%A}")

tanggal1 = dt.date(2005,10,10)

print(tanggal1)

print("input tanggal")
#harus dijadikan int untuk dimasukkan ke dt.date
#\t untuk tabs
tanggal = int(input("tanggal \t: "))
bulan = int(input("bulan \t\t: "))
tahun = int(input("tahun \t\t: "))

#format harus tahun-bulan-tanggal
tanggal_lahir = dt.date(tahun,bulan,tanggal)
print(f"Tanggal lahir anda : {tanggal_lahir}")

#untuk mencari umur
#.days untuk menghilankan days blablabla
umur_hari = hari_ini - tanggal_lahir
umur = umur_hari.days//365
print(f"umur anda adalah : {umur} tahun")



