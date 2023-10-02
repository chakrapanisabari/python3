demo_list= [1, 2, 3, 4, 5, 6,  7, 8]
# Printing test_list
print("The list is : ", demo_list)
counter = 0
print(len(demo_list))
for i in range(len((demo_list))):
    print(i, demo_list[i]) 

#Find the length of the list using naive method
for i in demo_list:
    counter += 1
print("Length of list using naive method is : ", counter)


# Define the list to be used for the demonstration
test_list = [1, 4, 5, 7, 8]
 
# Calculate the length of the list using a list comprehension and the sum function
# The list comprehension generates a sequence of ones for each element in the list
# The sum function then sums all the ones to give the length of the list
length = sum(1 for _ in test_list)
 
# Print the length of the list
print("Length of list using list comprehension is:", length)


# python code to find the length
# of list using enumerate function
list1 = [1, 4, 5, 7, 8]
s = 0
for i, a in enumerate(list1):
    s += 1
print(s)