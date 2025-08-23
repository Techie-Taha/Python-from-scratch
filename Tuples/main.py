numbers = (1, 2, 3) #we use [] to define list and () to define tuples
print(numbers.count(1)) #in the terminal we should see 1
#in tuples we can't change the item or insert new item
print(numbers[0]) #in the terminal we should see 1


number = (1, 6, 6, 6, 6666, 78)
print(number.count(6))

# we can also concatenate tuples
tuples1 =(1, 2, 3)
tuples2 = (4, 5, 6)
add = tuples1 + tuples2
print(add)