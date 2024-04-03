print("----------------Exericise 1-------------------")
# 1. Write a lambda function to calculate the square of a number.
calculate_square = lambda x: x**2
print("The square is: ", calculate_square(20), "\n")

print("----------------Exericise 2-------------------")
# 2. Write a function that takes a list of numbers and returns a list containing the squares of each number using lambda.
lst1 = [1,2,3,4,5,6,10,20,25]

calculate_square2 = list(map(lambda num: num**2, lst1))
print("Squared list is: ", calculate_square2, "\n")

print("----------------Exericise 3-------------------")
# 3. Write a function that returns a list of prime numbers up to a given number using lambda.
def check_prime(n):
  for i in range(2,n):
    if n % i == 0:
      return False
  return True

lst = [] ## append in the end?

num = 5
list_prime = list(filter(lambda n: [n for i in range(2,n) if n % i == 0], range(2, num+1)))


print("----------------Exericise 4-------------------")
# 4. Write a program that modifies a global variable inside a function
x = "It's Sunny"

def func():
  global x
  x = "It's Rainny :("

func()
print(x)

print("----------------Exericise 5-------------------")
# 5. Create a program that defines a function within another function and access variables from the outer function. (Often called Enclosing Scope)

def func1():
  season = "Spring" #local variable
  def change_season():
    print("We can't wait for: ", season) # access outer function's variable
  change_season()
func1()


print("----------------Exericise 6-------------------")
# 6. Create a program that defines a variable with the same name as a global variable inside a function and observe its scope.

test_var = 15

def change_var():
  test_var = 30
  print('local function is: ', test_var, "\n")

change_var()

print('global function is: ', test_var, "\n")
