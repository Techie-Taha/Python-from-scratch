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
