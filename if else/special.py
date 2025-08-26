num = int(input("Enter a number: "))

# if statement 1, this one will run independently
if num%4 == 0:
    print('succes')


# if statement 2, this one will run independently
if num >= 18:
    print("passed")

elif num == 18:
    print("failed")

elif num < 0:
    print("cooked")

else:
    print("RIP")