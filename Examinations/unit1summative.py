import sys #Imports the system module, used when exiting script

#Variables
incorrect_inRow = 0                 #This variable sets the baseline for how many questions the user has gotten wrong in a row
max_attempt = 2                     #This variable outlines how many questions the user has to get wrong in a row to exit the program
winnings = 0                        #This variable is the baseline for the winnings that the user earns when answering correctly


#Runs every time a question is answered; updates value of user winnings
def calc_winnings():
    global winnings                 #Defines winnings as a variable who's value can be changed can be changed in the other functions
    if winnings == 0:               #If this is the first question they got right, give them $1000
        winnings = 1000
    else:                           #Else, double their current earnings
        winnings = winnings*2

#Runs when 10 questions are completed or user has gotten 2 incorrect questions in a row
def leaving_show():
    print('You have ' + str(winnings) + ' in winnings')     #Prints the current subtotal of winnings
    taxed_winnings = float((winnings*0.63))     #Taxes the subtotal by a rate of 37%
    print('After taxes, you have $' + str(taxed_winnings) + ' in winnings')     #Prints the taxed subtotal of winnings
    relatives = input('We decided that you should share this money amongst your family\nHow many relatives do you have?: ')     #Asks user for input of how many family members to divide the earnings evenly upon
    final_winnings = taxed_winnings/float(relatives)      #Creates a variable with a value of the taxed subtotal divided by the amount of family members the user inputed
    charity = int(taxed_winnings)%int(relatives)            #Uses the modulo operator to find the remaninder of the money not divided amongst your family
    sys.exit("Congradulations, you are taking home $" + str(final_winnings) + " in winnings! As well, $" + str(charity) + " of your winnings are going to charity\nThanks for playing!")     #Exits the script with a message printing the total earnings for the contestant

#Runs as the first set of questions | All Mathematics related
def math():
    global incorrect_inRow      #Calls in the global definition of incorrect_inRow so it can be modified within the function and used in the main loop
    global calc_winnings        #Calls in the global definition of calc_winnings so it can be modified within the function and used in the main loop

    print('1. What is the product of 7 and 9?\nA. 16\nB. 21\nC. 63\nD. 0')      #Prints the first question set, divided across 5 lines
    answer_1 = input()      #Creates a variable storing the users input for the answer to the question
    if answer_1 == 'C' or answer_1 == 'c':      #Checks to see if answer is correct, in either lower/uppercase (Will be changed when I have more time)
        print('Correct')        #Prints if answer is correct
        incorrect_inRow = 0     #Resets value of incorrect_inRow
        calc_winnings()         #Calls function to update winnings
    else:
        print('Incorrect')      #Prints if answer is incorrect
        incorrect_inRow += 1    #Increases the value of incorrect_inRow by 1
        if incorrect_inRow == max_attempt:      #Checks to see if user has gotten 2 incorrect answers in a row
            print("Sorry, but you have gotten too many incorrect answers. Let's get you headed home") #Prints if above statement equates to True
            leaving_show()      #Calls the function that will calculate the total winnings and exit the python script
    print('What does the E in PEMDAS stand for?\nA. Energy\nB. Ejection\nC. Exponent\nD. Extravagant')      #Prints the second question set, divided across 5 lines
    answer_2 = input()      
    if answer_2 == 'C' or answer_2 == 'c':                              #Everything that was typed above also applies to anything
        print('Correct')                                                #down here, the system prints a question with a set of
        incorrect_inRow = 0                                             #answers, stores the input for that question, and checks
        calc_winnings()                                                 #to see if it is correct along with updating/checking
    else:                                                               #the value of variable incorrect_inRow to see if the user
        print('Incorrect')                                              #has gotten 2 incorrect answers in a row, resetting the value
        incorrect_inRow += 1                                            #of that variable if they get the question correct.
        if incorrect_inRow == max_attempt:
            print("Sorry, but you have gotten too many incorrect answers. Let's get you headed home")
            leaving_show()
    print('What property of numbers is shared by Addition and Multiplication?\nA. Distributive\nB. Associative \nC. Commutative\nD. Zero')
    answer_3 = input()
    if answer_3 == 'C' or answer_3 == 'c':
        print('Correct')
        incorrect_inRow = 0
        calc_winnings()
    else:
        print('Incorrect')
        incorrect_inRow += 1
        if incorrect_inRow == max_attempt:
            print("Sorry, but you have gotten too many incorrect answers. Let's get you headed home")
            leaving_show()

#Runs as the second set of questions | All History/Geography Related
def history():
    global incorrect_inRow
    global calc_winnings
    print('In what country is the Leaning Tower of Piza located?\nA. Iceland\nB. Canada\nC. Italy\nD. China')
    answer_1 = input()
    if answer_1 == 'C' or answer_1 == 'c':
        print('Correct')
        incorrect_inRow = 0
        calc_winnings()
    else:
        print('Incorrect')
        incorrect_inRow += 1
        if incorrect_inRow == max_attempt:
            print("Sorry, but you have gotten too many incorrect answers. Let's get you headed home")
            leaving_show()
    print('When did the war of 1812 begin?\nA. 2020\nB. 1776\nC. 1812\nD. 1945')
    answer_2 = input()
    if answer_2 == 'C' or answer_2 == 'c':              #Everything that was typed above also applies to anything
        print('Correct')                                #down here, the system prints a question with a set of
        incorrect_inRow = 0                             #answers, stores the input for that question, and checks
        calc_winnings()                                 #to see if it is correct along with updating/checking
    else:                                               #the value of variable incorrect_inRow to see if the user   
        print('Incorrect')                              #has gotten 2 incorrect answers in a row, resetting the value
        incorrect_inRow += 1                            #of that variable if they get the question correct.
        if incorrect_inRow == max_attempt:              
            print("Sorry, but you have gotten too many incorrect answers. Let's get you headed home")
            leaving_show()
    print('How many World Wars have there been?\nA. 3\nB. 24\nC. 2\nD. 6')
    answer_3 = input()
    if answer_3 == 'C' or answer_3 == 'c':
        print('Correct')
        incorrect_inRow = 0
        calc_winnings()
    else:
        print('Incorrect')
        incorrect_inRow += 1
        if incorrect_inRow == max_attempt:
            print("Sorry, but you have gotten too many incorrect answers. Let's get you headed home")
            leaving_show()

#Runs as the third set of questions | All Sports related
def sports():
    global incorrect_inRow
    global calc_winnings
    print('Who won the 2020 NBA Championship?\nA. Miami Heat\nB. San Antonio Spurs\nC. Los Angeles Lakers\nD. Milwaukee Bucks')
    answer_1 = input()
    if answer_1 == 'C' or answer_1 == 'c':
        print('Correct')
        incorrect_inRow = 0
        calc_winnings()
    else:
        print('Incorrect')
        incorrect_inRow += 1
        if incorrect_inRow == max_attempt:
            print("Sorry, but you have gotten too many incorrect answers. Let's get you headed home")
            leaving_show()
    print('What organization is in charge of the Professional Hockey League of the USA and Canada?\nA. The North American Hockey League\nB. The Canadian-American Hockey Association\nC. The National Hockey League\nD. The Canadian League')
    answer_2 = input()
    if answer_2 == 'C' or answer_2 == 'c':          #Everything that was typed above also applies to anything    
        print('Correct')                            #down here, the system prints a question with a set of
        incorrect_inRow = 0                         #answers, stores the input for that question, and checks
        calc_winnings()                             #to see if it is correct along with updating/checking
    else:                                           #the value of variable incorrect_inRow to see if the user
        print('Incorrect')                          #has gotten 2 incorrect answers in a row, resetting the value
        incorrect_inRow += 1                        #of that variable if they get the question correct.
        if incorrect_inRow == max_attempt:
            print("Sorry, but you have gotten too many incorrect answers. Let's get you headed home")
            leaving_show()
    print('What city do the "Dodgers" MLB team belong to?\nA. (NY) Brooklyn\nB. San Diego \nC. Los Angeles\nD. (NY) Manhattan')
    answer_3 = input()
    if answer_3 == 'C' or answer_3 == 'c':
        print('Correct')
        incorrect_inRow = 0
        calc_winnings()
    else:
        print('Incorrect')
        incorrect_inRow += 1
        if incorrect_inRow == max_attempt:
            print("Sorry, but you have gotten too many incorrect answers. Let's get you headed home")
            leaving_show()

#Final question, gives Atom the treatement it deserves
def editor():
    global incorrect_inRow
    global calc_winnings
    print("Which is the worst text editor for programming?\nA. Visual Studio Code\nB. PyCharm\nC. Atom\nD. The default Windows notepad")
    editor_answer = str(input())
    
    if editor_answer == 'C' or 'c':                 #Everything that was typed above also applies to anything
        print('Correct')                            #down here, the system prints a question with a set of
        incorrect_inRow = 0                         #answers, stores the input for that question, and checks
        calc_winnings()                             #to see if it is correct along with updating/checking
    else:                                           #the value of variable incorrect_inRow to see if the user
        print("Incorrect")                          #has gotten 2 incorrect answers in a row, resetting the value
        incorrect_inRow += 1                        #of that variable if they get the question correct.
        if incorrect_inRow == max_attempt:
            print("Sorry, but you have gotten too many incorrect answers. Let's get you headed home")
            leaving_show()


#MAIN LOOP
print("Welcome to the C-through triva show! The first topic will be mathematics, lets begin")

math()              #Calls the math function
history()           #Calls the history function
sports()            #Calls the sports function
editor()            #Calls the editor function
leaving_show()      #Calls the leaving_show function (Only if user answers all 10 questions)

#Everything below is a writeup of how the code actually runs/summary of the in's and out's

#The code first starts off with a print statement, which will print any variable in the form of a string in a line in the console.
#Then we proceed to call the trivia functions. Becides the questions and the specific answers pertaining to them, each triva function
#is identical for each other. For the most explanation you can click on the math module, however, each question utilizes 3 statements
#First off, the function will call the print statement and use '\n' to list the answers on multiple lines without having to call multiple
#print statements. Then, it will create a variable which stores the user input for their answer to the question just asked. The variable
#which is stored as a string will then be put into an if statement with a conditional seeing if the user input either 'C' or 'c'. There
#is a function in python which will allow you to not use an or statement when checking if an answer is lower or uppercase, however I did
#not want to spend today improving my code, but merely getting it done as it was quite difficult. If the answer is correct, the if statement
#will execute the code under it, which updates the winnings value by calling the calc_winnings() function, and reset the value of the variable
#incorrect_inRow. If the input of the user isn't 'C' or 'c' and the conditional of the If statement returns false, then it will skip to the else
#statement which will execute when the user inputs an incorrect answer. It will increase the value of the variable incorrect_inRow and then move
#onto the next if statement, which checks to see if the value of variable incorrect_inRow is equal to 2. If the conditional returns true, it will 
#call the function leaving_show(), if it returns false, the interpereter will skip over it and move onto the next question, which will repeat this
#process 9 more times. Each function, except for editor(), asks 3 questions related to their respective topics. One way or another, the function
#leaving_show() will be the last function called in the loop before exiting. If the user completes the main loop without the value of incorrect_inRow
#equating to 2, the leaving_show() function will be called at the end of the loop. It uses mathematical operators, variables and variable types, and
#print statements to insure the user recieves information about their gig at the trivia show. It will begin by calling the value of winnings which
#has been updated throughout the entire loop because of the trivia functions. It will then use the division, multiplication, and modulo mathematical
#operators in order to create values for the subtotal, taxed subtotal, total, and charital total. Using the mathematical operators we can assign
#integer or float variable types to the variables we created and print them out as strings in our print statement, as we do in the end of the loop.
#Finally, the sys.exit() function is called, delivering the message of the total and charital total along with a thanks to the user. The sys.exit()
#function is imported from the system module built into Python 3.9.0. It will halt execution of the main loop and exit the program. If using VS Code,
#The debugger will give error with the sys.exit function; however, if the program is ran without being debugged, it works like a charm.


#All of this code is original and written completely by Kapri O'Brien in 2020. Any use of this code without creator permission is prohibited
#Documents used in creation of this program are the Python 3.9 documentation available at https://docs.python.org/3/


    
