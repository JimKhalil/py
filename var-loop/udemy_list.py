list = [1,2,3,4]
list1 = [5,6,7,8]
list2 = list+list1
print(list2)
list2.append(9)
print(list2)
# pop itu sesuai index
list2.pop(1)
print(list2)
list2.append(2)
list2.sort()
print(list2)
list2.reverse()
print(list2)
print([1,'two',1.2])
print(([type(1), type('two'), type(1.2)]))