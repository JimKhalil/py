# kalau ini harus close
# myfile = open(r'D:\\Python\\udemy_python\\test.txt')
# file = myfile.read()
# print(file)
# file = myfile.close()

# or
with open(r'D:\\Python\\udemy_python\\test.txt', mode="a") as myfiles: 
    myfiles.write('\n new lines')

with open('dsadsadsa.txt',mode="w") as myfiles:
    myfiles.write("\n test new files")

# mode r untuk read
# mode w untuk write
# mode a untuk append