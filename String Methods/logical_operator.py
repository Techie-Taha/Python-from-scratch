has_high_income = True
has_good_habit = True

eligibility = "eligible for loan"

if has_high_income and has_good_habit:
    print(eligibility)
else:
    print("not eligible")

has_criminal_record = True
has_murder_record = False

eligibility = "eligible for citizenship"

if has_high_income or has_good_habit:
    print(eligibility)
else:
    print("not eligible")
# since both true, also because of and operator it will return eligible 
# if one of the statement is false, also has and operator it will return false not eligible
# if one of the statement is false, also has or operator it will return True because in that case only one of the condition needs to be true eligible
# and not operator makes true statement false, and false statement true
