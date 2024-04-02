import random
# 5. Optional Lab - Guessing game
"""""
GUESSING GAME: COMPUTER GENERATES A 3 DIGIT RANDOM NUMBER, USER WILL INPUT GUESSES UNTIL NUMBER IS CORRECT.
USER WILL RECEIVE HINTS OF HOW CLOSE IT IS TO GET THE CORRECT NUMBER.
"""""
def generate_3digit_num():
# computer_choice = #random 3 digit number that cannot repeat
    three_digits_number = [0,0,0]
    while three_digits_number[0] == 0:
        digits = list(range(10))
        random.shuffle(digits)
        three_digits_number = digits[:3]
            # computer_choice = int(''.join([str(item) for item in three_digits_number]))
    return three_digits_number

#main game function execution
def guess_number_game():

    computer_choice = generate_3digit_num()
    print("Computer choice is {}".format(computer_choice))

    #scope of user choice function()
    #convert user input to list, to compare equaly with computer choice
    user_choice = list(input("Guess the 3 digit number the computer selected:\n"))
    user_choice = [int(item) for item in user_choice]
    print("Your choice is {}".format(user_choice))

    #comparison between both lists
    all_match = False
    some_match = False
    found = False

    for i in range(len(user_choice)):
        for j in range(len(computer_choice)):
            if user_choice[i] == computer_choice[j]:
                some_match = True
                found = True
                if i == j:
                    all_match = True
        if not found:
            all_match = False
    
    # match output
    if all_match:
        print("Match!")
    elif some_match:
        print("Close!")
    else:
        print("Nope!")


guess_number_game()