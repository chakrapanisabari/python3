a=("demo", '1234', '2234')
print(a)
print(a[1])
# a.pop() #Throws error due to tuple
# a.append('23') #Throws error due to tuple#
print('##############################################################################################')
tuple1=1,3,4,5
tuple2 = ('sabari','dad',"sed")
print(type(tuple2))
print("First tuple:", tuple1)
print("Second Tuple:", tuple2)
list1=[1, 45, "Sabarish", 89.0, 34]
print("Type of list1", type(list1))
print(list1);
tuple3=tuple(list1)
print(tuple3)
print(type(tuple3))

tuple4=tuple1,tuple2,tuple3
print(tuple4)
print('##############################################################################################')

mix=1,2,list1
print(type(mix))

a,b=tuple4
print(a)