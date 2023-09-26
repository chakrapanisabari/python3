# Assigning string to a variable
a = 'This is a string'
print (a)
b = "This is a string"
print (b)
c= '''This is a string'''
print (c)

str1 = ' My name is sabari'
str2 = "I'm Sabari lives in Kumbakonam"
str3 = '''I am 
Sabari lives
in Kumbakonam'''

print("Single quote string:",str1)
print("Double quote string:",str2)
print("Multiline string using three quotes:",str3) #Multiline string

#Indexing

print("character with negative index:", str1[-2])
print("character with positive index:", str1[1])

#slicing using the slicing operator : colon
print("Slice character with positive index:", str1[1:2])
print("Slice character with negative index:", str1[-1:])

#Reverse a string
string1="ChakrapaniSabariR"
print("Reversed String using index:", string1[::-1])
string1="".join(reversed(string1))
print("Reversed String using join and reveresed function:", string1)


# Python Program snippet to update character of a String
 
string1 = "My Name is Sabari"
print("Initial String: ")
print(string1)
 
# Updating a character of the String 
# As python strings are immutable, they don't support item updation directly there are following two ways
#1
list1 = list(string1)
print(list1)
list1[2] = 'p'
string2 = ''.join(list1)
print("\nUpdating character at 2nd Index: ")
print(string2)
 
#2
string3 = string1[0:2] + 'p' + string1[3:]
# print(string1[0:2])
# print(string1[3:])
# print(string1[1:])
print(string3)

#Deletion is possible using del keyword
#1
print(string3)
string_delete_list=list(string3)
del string_delete_list[2]
string_delete_list_new=''.join(string_delete_list)
print(string_delete_list_new)
#2
print(string3)
string_delete=string3[0:2] + ' ' + string3[3:]
print(string_delete)


