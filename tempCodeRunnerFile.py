import datetime as dt

#format string

nama = "abi"
format_str = (f"muhammad haris maulana koliq {nama}")
print(format_str)

#harus import untuk menggunakan fungsi date

#kenapa jadi dt karena datetime diganti menjadi variable dt

hari_ini = dt.date.today()

print(hari_ini)

print(f"hello {hari_ini:%A}")

tanggal = dt.date(2005,10,10)

print(tanggal)