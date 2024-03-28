# Date 03/27
# 1. Write a program that takes two integers as input, base and exponent, and calculates the power using loops.
# 2. Write a program that calculates the sum of all elements in a given tuple.
# 3. Write a program that creates a new tuple containing only the even numbers from a given tuple of integers.
# 4. Write a program that merges two dictionaries into a single dictionary. If a key is common to both dictionaries, the value from the second dictionary should be used.
# 5. Write a program that takes a list of integers as input and uses list comprehension to create a new list containing only the even numbers from the original list.
# 6. Write a program that takes a string as input and prints its reverse.

#1. exercise
def calculate_power():
 #get user inputs
 base_num = int(input("Type the base number:\n"))
 exp_num = int(input("Type the exponent number:\n"))
 #set iteration start from 1 and base_num value
 result = 1
 #loop - repeat iteration (multiplication of base_num for itself) for the counting of exp_num
 for _ in range(exp_num):
  result *= base_num
 return print("Base {} and exponent {} = {}".format(base_num,exp_num,result))

calculate_power()

# #2. exercise
# def sum_tup(tup):
#  #innitialize sum in 0
#  sum = 0

#  #iterate through each element in tuple and sum
#  for item in tup:
#   sum += item
#  return sum

# tup = (1,2,3,4,5,20)
# print(sum_tup(tup))

#3. exercise
# def extract_even(tup):
#  tup_list = list(tup)
#  even_list = []

#  for i in tup_list:
#   if i % 2 == 0:
#    even_list.append(i)

#  tup_even_list = tuple(even_list)
#  return tup_even_list

# tup = (1,2,3,4,5,6)
# print(extract_even(tup))

#4 exercise

# def merge_dict(dict1,dict2):
#  iteration through both dictionaries, going first through dict2 to 
#  for item in dict2.keys():
#   compare key-value pairs #update dict1 value with dict2 value, when common value found
#   dict1[item]=dict2[item]
#  return dict1

# dict1 = {'key1': 1, 'key2': 2, 'key3': 3, 'key5': 5}
# dict2 = {'key3': 10, 'key4': 4}
# merged_dict = merge_dict(dict1,dict2)

# print(merged_dict)

#5 exercise
# list = []

#define amount of elements on list
# items_amount = int(input("Type amount of elements on the list:\n"))
# for i in range(items_amount):
# add elements to the list
#  list.append(int(input("Enter the integer numbers to add to the list:\n")))

# print("The even list is:", [item for item in list if item % 2 == 0])

#6 exercise
# def main():
   #get user input
#  user_str = str(input("Type a text:\n"))
#  def reverse_str(str):
#   return str[::-1]
 
#  reversed_str = reverse_str(user_str)
#  print(reversed_str)

# main()