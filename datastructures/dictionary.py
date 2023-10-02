dict={1:'sabari', 2:'dad'}
print(dict)
print(type(dict))

dict1={1:'sabari',2:'Daddy',3:'Mom'}
print(dict1)

dict2={1:dict1,2:'sabari','daddy':'valurer'}
print(dict2)

print(dict2['daddy'])
#Access the dictionary using get method
print("Demo answer:", dict2.get(1),sep='/',end="\n")
print(dict2[1][2])