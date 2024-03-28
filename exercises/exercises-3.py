#SET
# x = set()
# x.add(1)

# print(x)

# #Does not allow duplicates
# y = {1,2,3}
# y.add(3)

# print(y)

# if 1 == 2:
#   print("yes")
# elif 3 == 3:
#   print("middle")
# else:
#   print("last")

#Loops

#list
# sequence = [1,2,3,4,5,6,7,8,9,10]

# for item in sequence:

#  print(item+item)

#dict
 
# ages = {
#  'John': 5,
#  'Doe': 8,
#  'Moe': 3
# }

# for key in ages:
#  print('This is the key:')
#  print(key)
#  print('This is the value:')
#  print(ages[key])
#  print('\n')

mypairs = [(1,10), (2,20), (3,30)]

for item1,item2 in mypairs:
  print(item1, item2)

mypairs2 = [(1,10), (2,20), (3,30)]

for item1 in mypairs2:
  print(item1[0], item1[1])  

#while loop

# i = 1

# while i < 5:
#  print('i is: {}'.format(i))
#  i = i + 1

# x = [1,2,3]

# out = []

# for item in x:
#  out.append(item**2)

# print(out)

# #in a single line

# print([item**2 for item in x])