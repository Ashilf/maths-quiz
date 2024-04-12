#Math Quiz
import random


#Definding the players username to keep track of the score.

name = input("What Is Your Name? \n").capitalize()

#displaying Result for user
def display_result(total, correct):
    global percentage
    if total > 0:
        result = correct / total
        percentage = round((result * 100), 2)
    if total == 0:
        percentage = 0
    print("You answered", total, "questions with", correct, "correct.")
    print("Your score is ", percentage, "%")

#Checks users enter yes (y) or no (n)
def yes_no(question):

        while True:
            response = input(question).lower()
            print(f"You answered {response} to the question")

            if response == "yes" or response == "y":
                return True

            elif response == "no" or response == "n":
                return False

            else:
                print("please enter yes/no")


#title to the start of the QUIZ
def display_intro():
    print()
    print("Welcome To The Math Quiz " +name+ "!")
    print()

def get_float(question):
    while True:
        try:
            response = float(input(question))
            return response
        except:
            print("ERROR: Please responed in numbers! ")


#Prints out Instructions or user
def instructions():
    print("--------------------------------instructions----------------------------------------")
    print("                                                                                    ")
    print("        In this quiz you will be have to answer a series of questions, ")
    print("   depending on how many you get right will be your total at the end of the game.")
    print("                                                                                    ")
    print("------------------------------------------------------------------------------------")


def game_sure():
    game = yes_no("are you sure? ")
    if game:
        main()
    else:
        print()


#menu of quiz/type of question
def display_menu():


    menu_list = ["1. Addition", "2. Subtraction", "3. Multiplication",
                 "4. Integer Division", "5. Exit"]
    print(menu_list[0])
    print(menu_list[1])
    print(menu_list[2])
    print(menu_list[3])
    print(menu_list[4])


def display_separator():
    print("-" * 24)
#Getting user answer for deciding on questions


def get_user_input(question):
    user_input = input(question)
    user_input = int(user_input)
    while user_input > 5 or user_input <= 0:
        print("Invalid menu option.")
        user_input = int(input("Please try again: "))
    else:
        return user_input


#checking user solutions/getting the users solution
def get_user_solution(problem):
    print("Enter your answer")
    print(problem, end="")
    result = int(input(" = "))
    return result

def check_solution(user_solution, solution, count):
    if user_solution == solution:
        count = count + 1
        print("Correct.")
        return count
    else:
        print("Incorrect.")
        return count


def get_user_response():
    user_input = int(input("Please Select one of the following: \n"))
    while True:
        if user_input == 1:
            Addition()
            break

        elif user_input == 2:
            Subtraction()
            break
        elif user_input == 3:
            Multiplication()
            break

        elif user_input == 4:
            Integer_Division()
            break

        elif user_input == 5:
            exit()
        break

    while user_input > 5 or user_input <= 0:
        print("Invalid menu option.")
        user_input = int(input("Please try again: "))



def exit():
    print("Goodbye")


def Addition():
    while True:
        try:

            rnds = int(input("How many questions would you like?: 5, 10, 15, or 20? "))
            if rnds == 5 or rnds == 10 or rnds == 15 or rnds == 20 or rnds == print():
                break
            else:
                print("ERROR: INVALID INPUT! Please enter 5, 10, 15 0r 20. ")

        except ValueError:

            print("ERROR: INVALID INPUT! Please enter 5, 10, 15 0r 20. ")
#menu/questions
def menu(index, count):
    number_one = random.randrange(1, 21)
    number_two = random.randrange(1, 21)
    if index == 1:
        problem = str(number_one) + " + " + str(number_two)
        solution = number_one + number_two
        user_solution = get_user_solution(problem)
        count = check_solution(user_solution, solution, count)
        return count
    elif index == 2:
        problem = str(number_one) + " - " + str(number_two)
        solution = number_one - number_two
        user_solution = get_user_solution(problem)
        count = check_solution(user_solution, solution, count)
        return count
    elif index == 3:
        problem = str(number_one) + " * " + str(number_two)
        solution = number_one * number_two
        user_solution = get_user_solution(problem)
        count = check_solution(user_solution, solution, count)
        return count
    else:
        problem = str(number_one) + " // " + str(number_two)
        solution = number_one // number_two
        user_solution = get_user_solution(problem)
        count = check_solution(user_solution, solution, count)
        return count





def Subtraction():


    while True:
        try:

            rnds = int(input("How many questions would you like?: 5, 10, 15, or 20? "))
            if rnds == 5 or rnds == 10 or rnds == 15 or rnds == 20 or rnds == print():
                break
            else:
                print("ERROR: INVALID INPUT! Please enter 5, 10, 15 0r 20. ")

        except ValueError:

            print("ERROR: INVALID INPUT! Please enter 5, 10, 15 0r 20. ")



def Multiplication():

    while True:
        try:

            rnds = int(input("How many questions would you like?: 5, 10, 15, or 20? "))
            if rnds == 5 or rnds == 10 or rnds == 15 or rnds == 20 or rnds == print():
                break
            else:
                print("ERROR: INVALID INPUT! Please enter 5, 10, 15 0r 20. ")

        except ValueError:

            print("ERROR: INVALID INPUT! Please enter 5, 10, 15 0r 20. ")

def Integer_Division():

    while True:
        try:

            rnds = int(input("How many questions would you like?: 5, 10, 15, or 20? "))
            if rnds == 5 or rnds == 10 or rnds == 15 or rnds == 20 or rnds == print():
                break
            else:
                print("ERROR: INVALID INPUT! Please enter 5, 10, 15 0r 20. ")

        except ValueError:

            print("ERROR: INVALID INPUT! Please enter 5, 10, 15 0r 20. ")



def main():
    display_intro()
    display_menu()
    display_separator()

    option = get_user_input("Enter your choice: \n")
    total = 0
    correct = 0
    while option != 5:
        total = total + 1
        correct = menu(option, correct)
        option = get_user_input('Please enter a number between 1 and 5 \n')

        print("Exit the quiz.")
        display_separator()
        display_result(total, correct)




#print instructions if user answers: Yes/Y/yes

response = yes_no("Do you want to read the instructions? \n")

if response:
    instructions()
print()





while True:
    try:
        start_game = yes_no("hey " +name+ " Would You Like To Start The Quiz? \n")
        if start_game:
           main()


        else:
            print()
            print("Don't waste my time")
            print()
            break

    except ValueError:
        print()
        print("ERROR: you did not choose a vaild response, please try again. ")
        print()














