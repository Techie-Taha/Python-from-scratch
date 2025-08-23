name = "Taha"
print('Taha' in name) #in operator works like a boolean expression and in the terminal we will see true
print('taha' in name) #here we will see false in the terminal since I put lowercase t


num = ["Taha", 65, "Apple", 76.5, "Nishat", False]
if "taha" in num:
    print("True")
else:
    print("false")


tuples1 =(1, 2, 3)
tuples2 = (4, 5, 6)

print(1 in tuples1)
print(7 in tuples2)
