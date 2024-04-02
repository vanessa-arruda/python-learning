print("--------------------next exercise-1------------------------\n")
# 1. Given a list of integers, return True if the sequence of numbers 1, 2, 3 appears in the list somewhere.

def list_check(my_list):
    #iterate through entire list "-2" meaning that I will always pick min of 3 elements, considering entire list length
    for i in range(len(my_list)-2):
        if my_list[i] == 1 and my_list[i+1] == 2 and my_list[i+2] == 3:
            return True
    return False

#tests
test_cases1 = [[1,2,3,0,2,1,2], [1,0,3,1,2,3], [], [1,2,3], [1,2], [1,2,3,1,2,3]]
result_cases1 = [list_check(case) for case in test_cases1]
print(result_cases1)


print("--------------------next exercise-2------------------------\n")
# 2. Given a string, return a new string made of every other character starting with the first, so "Hello" yields "Hlo".
# def change_str(str):
    # new_str = ""
    # if len(str) == 0:
    #     return "You gave me no string to change."
    # else:
    #     for i in range(len(str)):
    #         if i % 2 == 0:
    #             new_str += str[i]
    #     print(new_str)

def change_str(str):
    # new_str = ""
    return str[::2] # solution with 1 line
        
    
#tests
test_cases2 = ["Hello", "Vanessa", "Va", ""]
result_cases2 = [change_str(case) for case in test_cases2]
print(result_cases2)

#expected "Hlo"
#expected "Vnsa"
#expected "V"
#expected "You gave me no string to change."

print("--------------------next exercise-3------------------------\n")
# 3. Given a string, return a string where for every char in the original, there are two chars

def double_chars(str):
    new_str = ""
    if len(str) == 0:
        return print("You gave me no string to change.")
    else:
        for i in range(len(str)):
            new_str += str[i] * 2
        print(new_str)
    # return ''.join([char*2 for char in str]) # other solution
#tests
double_chars("Hi") #expected "HHii"
double_chars("Python") #expected "PPyytthhoonn"
double_chars("") #expected "You gave me no string to change."

print("--------------------next exercise-4------------------------\n")
# 4. Return the number of even integers in the given array/list

def count_evens(int_list):
    even_count = 0
    for item in int_list:
        if item % 2 == 0:
            even_count += 1
    print(even_count)

    # return sum(1 for num in int_list if num % 2 == 0) 

#test
count_evens([1,2,3,4,6,8,10]) #expected 5
count_evens([]) #expected 0
count_evens([2]) #expected 1

print("--------------------next exercise-5------------------------\n")
# 5. Optional Lab - Guessing game
# As it is a complete project - it is in a separate file.
