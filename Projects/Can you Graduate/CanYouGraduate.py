#User inputs number of credits they have
print("How many high school credits do you have?")
credits = input()

print("Have you taken AP Computer Science Principles? Respond with (Y/N)")
comp_sci = input()

can_graduate = str(comp_sci) == "Y" or str(comp_sci) == "y"

print("Can you graduate?: " + str(can_graduate))