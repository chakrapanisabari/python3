a= ['1', 'dad', '123', 'demo']
print(a[1])
a.append('Demo12345')
print(a);
a.pop()
print(a);

list1 = ['sabari', 1 , 2 , 4 , 'Daddy', 'Gold']
print("Access entire list", list1)
print("Access particular element in the list using index:", list[3])
list2 = list1
list2.pop()
print(list2)
print(list1)
list2.append('Demomomo')
list2.append(2)
print(list2)
list2.append(list1)
print(list1)
print(len(list2))
print(len(list1))
for i in range(5,11):
    list2.append(i)
print(list2)
list2.append((2,4))
print(list2)
del list2
print(list1)