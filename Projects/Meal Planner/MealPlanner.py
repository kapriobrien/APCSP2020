import random

def savory_breakfast():
    #Creates a list of savory breakfast items
    breakfast_savory_list = ['How about some Avacado Toast?', 'You ever tried Huevos Rancheros?', 'Bacon, Eggs & Toast never goes wrong']

    #Chooses one item from the list of savory breakfast items
    breakfast_savory_rec = random.choice(breakfast_savory_list)

    #Prints out the randomly selected savory breakfast reccomendation
    print(str(breakfast_savory_rec))

def sweet_breakfast():
    #Creates a list of sweet breakfast items
    breakfast_sweet_list = ["I think some Pancakes would suit you", "Dunkin Donuts has a sale this week!", "By chance, do you have Lucky Charms in your pantry?"]

    #Chooses one item from the list of sweet breakfast items
    breakfast_sweet_rec = random.choice(breakfast_sweet_list)

    #Prints out the randomly selected sweet breakfast reccomendation
    print(str(breakfast_sweet_rec))

def quick_lunch():

    lunch_quick_list = ['Try making a turkey sandwich', 'Salad is a Cheap, Easy, Healthy, & Quick option', 'Hot dogs and potato chips are always great!']
    lunch_quick_rec = random.choice(lunch_quick_list)

    print(str(lunch_quick_rec))

def time_lunch():

    lunch_time_list = ['A Bacon and Scallion grilled cheese with Tomato Bisque is great', 'The Philly Cheesesteak is a great Sandwich', "Try your hand at a Rice Bowl"]
    lunch_time_rec = random.choice(lunch_time_list)

    print(str(lunch_time_rec))

def light_dinner():
    
    dinner_light_list = ['Grilled Chicken on top of Greens is Delicious', 'Seared Salmon with asparagus is great', 'Try your hand at Rattatouille!']
    dinner_light_rec = random.choice(dinner_light_list)

    print(str(dinner_light_rec))
    
def heavy_dinner():
    
    dinner_heavy_list = ['A pot roast with mashed potatoes always reminds me of home', 'Steak with Rice, Beans, Chorizo, Chicharon and Avocado will never let you down', "A hearty stew will leave you satisfied for the rest of the day"]
    dinner_heavy_rec = random.choice(dinner_heavy_list)

    print(str(dinner_heavy_rec))

def user_choice_breakfast():

    #If the User inputs 1 for Breakfast, it will read this if statement
    if str(meal_choice) == "Breakfast" or str(meal_choice) ==  "breakfast":
    
        print("Are you in the mood for something savory or sweet?")
       
        break_choice = input()

        #If the user selects 1 for Savory, it will read this if statement
        if str(break_choice) == "savory" or str(break_choice) == "Savory":
        
            savory_breakfast()
    
        #If the user selects 2 for Sweet, it will read this if statement
        elif str(break_choice) == "sweet" or str(break_choice) == "Sweet":

            sweet_breakfast()

def user_choice_lunch():
    #If the user inputs 2 for Lunch, it will read this if statement
    if str(meal_choice) == "Lunch" or str(meal_choice) == "lunch":
    
        print("Did you need something quick or do you have some time?")
    
        lunch_choice = input()

        if str(lunch_choice) == "quick" or str(lunch_choice) == "Quick":

            quick_lunch()

        elif str(lunch_choice) == "time" or str(lunch_choice) == "Time" or str(lunch_choice) == "have time" or str(lunch_choice) == "Have Time" or str(lunch_choice) == "Have time" or str(lunch_choice) == "Have Time":

            time_lunch()

def user_choice_dinner():

    #If the user inputs 3 for Dinner, it will read this if statement
    if str(meal_choice) == "Dinner" or str(meal_choice) == "dinner":
    
        print("Are you feeling like eating light today, or do you want a full meal?")

        dinner_choice = input()

        if str(dinner_choice) == "light" or str(dinner_choice) == "Light":

            light_dinner()

        elif str(dinner_choice) == "full meal" or str(dinner_choice) == "Full meal" or str(dinner_choice) == "Full Meal " or str(dinner_choice) == "full Meal" or str(dinner_choice) == "full" or str(dinner_choice) == "Full":

            heavy_dinner()

print("What meal are you in the mood for right now? Breakfast, Lunch, or Dinner")
meal_choice = input()

#If the user inputs 1 for Breakfast, the program will execute this function
user_choice_breakfast()

#If the user inputs 2 for Lunch, the program will execute this function
user_choice_lunch()

#If the user inputs 3 for Dinner, the program will execute this function
user_choice_dinner()