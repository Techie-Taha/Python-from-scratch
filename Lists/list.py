# write a program to find the largest number in a list
numbers = [3, 7, 2, 8, 4, 10, 17, 18, 20]
largest_number = numbers[0] #just an assumption
for number in numbers:
    if number > largest_number:
        largest_number = number
print(largest_number)