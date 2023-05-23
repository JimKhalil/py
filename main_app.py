#function

def hello_world():
        print("hello world")

hello_world()

# function dengan argument/parameter input``

'''
template
def nama_fungsi():
'''

nama = input("siapakah nama anda ?")
a = int(input("jumlah yang akan diulang ?"))
i = 0
def hello_world2(nama,i,a) :
    while i < a :
        i+=1
        print(f"ini nama yang diulan {nama}",i)
hello_world2(nama,i,a)

# def function(angka1=input('input1'), angka2=input 2)

def tri_recursion(k):
     if(k > 0):
        result = k + tri_recursion(k - 1)
        print(result)
     else:
        result = 0
        return result

print("\n\nRecursion Example Results")
tri_recursion(6)
