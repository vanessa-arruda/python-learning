import random #for exercise 5
# 1. Given a list of integers, return True if the sequence of numbers 1, 2, 3 appears in the list somewhere.

def listCheck(my_list):
    #iterate through entire list "-2" meaning that I will always pick min of 3 elements, considering entire list length
    for i in range(len(my_list)-2):
        if my_list[i] == 1 and my_list[i+1] == 2 and my_list[i+2] == 3:
            return print(True)
    else:
        return print(False)

#tests
list1 = [1,2,3,0,2,1,2] 
list2 = [1,0,3,1,2,3]
list3 = []
list4 = [1,2,3]
list5 = [1,2]
list6 = [1,2,3,1,2,3]
listCheck(list1) #expected True
listCheck(list2) #expected True
listCheck(list3) #expected False
listCheck(list4) #expected True
listCheck(list5) #expected False
listCheck(list6) #expected True

print("--------------------next exercise-2------------------------\n")
# 2. Given a string, return a new string made of every other character starting with the first, so "Hello" yields "Hlo".

def changeStr(str):
    new_str = ""
    if len(str) == 0:
        return print("You gave me no string to change.")
    else:
        for i in range(len(str)):
            if i % 2 == 0:
                new_str += str[i]
        print(new_str)
    
#tests
changeStr("Vanessa") #expected "Vnsa"
changeStr("Va") #expected "V"
changeStr("") #expected "You gave me no string to change."

print("--------------------next exercise-3------------------------\n")
# 3. Given a string, return a string where for every char in the original, there are two chars

def doubleChars(str):
    new_str = ""
    if len(str) == 0:
        return print("You gave me no string to change.")
    else:
        for i in range(len(str)):
            new_str += str[i] * 2
        print(new_str)

#tests
doubleChars("Hi") #expected "HHii"
doubleChars("Python") #expected "PPyytthhoonn"
doubleChars("") #expected "You gave me no string to change."

print("--------------------next exercise-4------------------------\n")
# 4. Return the number of even integers in the given array/list

def count_evens(int_list):
    even_count = 0
    for item in int_list:
        if item % 2 == 0:
            even_count += 1
    print(even_count)

#test
count_evens([1,2,3,4,6,8,10]) #expected 5
count_evens([]) #expected 0
count_evens([2]) #expected 1

print("--------------------next exercise-5------------------------\n")
# 5. Optional Lab - Guessing game
#import random in line 1
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
def guessNumberGame():

    computer_choice = generate_3digit_num()
    print("Computer choice is {}".format(computer_choice))

    #scope of user choice function()
    #convert user input to list, to compare equaly with computer choice
    user_choice = list(input("Guess the 3 digit number the computer selected:\n"))
    user_choice = [int(item) for item in user_choice]
    print("Your choice is {}".format(user_choice))


guessNumberGame()