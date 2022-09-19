
# This makes a pause in between prints
from time import sleep

# This Makes the quiz work and that jazz
def new_game():

    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("------------------------------")
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess = input("Enter (A, B, C, or D): ").upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key), guess)
        question_num += 1

# This Makes putting in the answers in work
def check_answer(answer, guess):

    if answer == guess:
        print("CORRECT")
        return 1
    else:
        print ("WRONG")
        return 0


# This Makes The Text Look Snazzy
def statement_generator(statement, decoration):

    sides = decoration * 3

    statement = "{} {} {} ".format(sides, statement, sides)
    top_bottom = decoration * len(statement)

    print(top_bottom)
    print(statement)
    print(top_bottom)

    return ""

# This Tells the user how to play and stuff
def instructions():
    print()
    statement_generator(" Hello Welcome To The Quiz Quest Show where we will be testing your Minecraft knowledge ", "*")
    print()
    sleep(3)
    statement_generator(" We Will be asking 10 Questions and judging how much you know about Minecraft ", "-")
    print()
    sleep(3)
    statement_generator(" To play you will answer a question by typing 1 for question 1 and 2 for question 2 ", "?")
    print()
    sleep(3)
    statement_generator(" Also If you want to exit the Quiz Quest at anytime you just need to type in 'xxx' Have Fun :) ", "7")
    print()
    sleep(3)

# These are the questions for the quiz
questions = {
  "Which Structure Can you not get enchanted books from": "C",
  "Which Minecraft World Seed is more famous": ""
  ""
  ""
  ""
  ""
  ""
  ""
  ""
  " "
}

options = [["A. Stronghold", "B. Shipwreck", "C. Ruined Nether Portal", "D. "],
           ["A. ", "B. 2151901553968352745" "C. 47886854082066804"],
           ]

instructions()

# This is to have a name to the player and To make the player think they have importance
name = input(" Please enter a Name or Nickname : ")
print()
sleep(1)
print()
sleep(1)
print(" Hello {} Thank You for Participating in this game".format(name))
print()
sleep(2)

# This code is to make the quiz and for it to work

point = 0

rounds_played = 0

print()




