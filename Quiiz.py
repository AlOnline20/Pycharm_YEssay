
# This makes a pause in between prints
from time import sleep

# This Makes the quiz work and that jazz
def new_game():

    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("------------------------------")
        print()
        print("------------------------------")
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess = input("Enter (A, B, C, or D): ").upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key), guess)
        question_num += 1

    display_score(correct_guesses, guesses)

# This Makes putting in the answers in work
def check_answer(answer, guess):

    if answer == guess:
        print("CORRECT +1 Point")
        return 1
    else:
        print("WRONG +0 Points ")
        return 0

# This is to display the score
def display_score(correct_guesses, guesses):
    print("------------------------------")
    print()
    print("RESULTS")
    print()
    print("------------------------------")
    print()

    print("Answers:  ", end=" ")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("Guesses:  ", end=" ")
    for i in guesses:
        print(i, end=" ")

    score = int((correct_guesses/len(questions))*100)
    print("Your score is: "+str(score)+"%" " Out of 100%")

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
    statement_generator(" To play you will answer Multiple choice questions with A/B/C or D ", "?")
    print()
    sleep(2)
    statement_generator(" If you put in the wrong input you will automatically Be wrong ", "W")
    print()
    sleep(3)
    statement_generator(" Have Fun :) ", "7")
    print()
    sleep(3)

# These are the questions for the quiz
questions = {
  "Which Structure Can you not get enchanted books from": "C",
  "Which Minecraft World is more famous": "B",
  "Who is the most famous minecraft Youtuber of all time": "A",
  "How much Pieces of Leather/Iron/Gold/Diamonds do you need to make a full set of Armor": "D",
  "When did microsoft buy minecraft": "A",
  "How do you breed Chickens": "C",
  "When did Minecraft Pocket Edition come out": "D",
  "Which Game Is there a reference to Minecraft": "B",
  "When Did Minecraft start getting popular again": "A",
  "Who won the first ever minecraft championships": "D"
}

# These are the options for the questions.
options = [["A. Stronghold", "B. Shipwreck", "C. Ruined Nether Portal", "D. Bastion"],
           ["A. Stampys lovely world", "B. Notch's Head", "C. DanTDMs mod showcase world", "D. Minecraft Tutorial World "],
           ["A. DanTDM", "B. Stampylongnose", "C. Technoblade", "D. CaptianSparklez"],
           ["A. 23", "B. 25", "C. 22", "D. 24"],
           ["A. 2014", "B. 2015", "C. 2013", "D. 2016"],
           ["A. Wheat", "B. Carrot", "C. Seeds", "D. Sweet Berries"],
           ["A. August 15 2011", "B. July 27 2012", "C. August 17 2012", "D. August 16 2011"],
           ["A. Doom64", "B. Terraria", "C. Halo Combat Evolved", "D. Cuphead"],
           ["A. 2019", "B. 2020", "C. 2021", "D. 2018"],
           ["A. Lime Llamas", "B. Green Guardians", "C. Cyan Creepers", "D. Purple Pandas"]]

instructions()

# This is to have a name to the player and To make the player think they have importance
name = input(" Please enter a Name or Nickname : ")
print()
sleep(1)
print()
sleep(1)
print(" Hello {} and welcome to the QUIZ QUEST".format(name))
print()
sleep(1)

# This code is to make the quiz and for it to work

point = 0

rounds_played = 0

print()
new_game()
print()
sleep(2)

print("Thank you {} for playing this game,  Goodbye :)".format(name))
