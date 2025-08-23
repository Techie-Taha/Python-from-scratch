# write a program to find the largest number in a list

numbers = [1, 44, 87, 98, 25] # This line creates a list called numbers that contains five integers: 1, 44, 87, 98, and 25.
large = numbers[0] # This initializes the variable large with the first number in the list (which is 1). The idea is to assume the first number is the largest for now, and then compare it with the rest of the numbers in the list

for number in numbers: # This starts a for loop that will go through each number in the numbers list one by one. On each loop iteration, the variable number holds the current item from the list.
    if number > large: # This checks if the current number is greater than the current value stored in large. If this is true, it means we've found a new, larger number.
        large = number # If the condition in the if statement is true, this line updates large to hold the new larger value.
print(large)