lists = [2, 2, 4, 6, 3, 4, 6, 1]
new_list = []
for number in lists:
    if number not in new_list:
        new_list.append(number)
new_list.sort() #it will sort the list in a correct form
print(new_list)

