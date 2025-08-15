weight = input("What's your weight? ")
unit = input("lbs or kg: ")
if unit == 'lbs':
    weight_in_kg = 0.454 * float(weight)
    print(f' Your weight is {weight_in_kg} kilogram')
else:
    weight_in_lbs = 2.205 * int(weight)
    print(f' Your weight is {weight_in_lbs} pounds')