
print("Is it a weekday? Respond with (Y/N)")
is_weekday = input()

print("Is it a holiday? Respond with (Y/N)")
is_holiday = input()

no_school_today = is_holiday == "Y" or is_weekday == "N"

print('No school today?: ' + str(no_school_today))