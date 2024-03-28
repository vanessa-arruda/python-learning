# print("Hello World!")

# def make_abba(a, b):
#  return a+b+b+a

# print(make_abba("van", "eve"))

# def make_tags(tag, word):
#   return "<"+ tag + ">" + word + "<" + tag + "/>"

# print(make_tags("p", "baby"))

# def make_out(out, word):
#   if len(out) == 4:
#     return out[0]+out[1]+word+out[2]+out[3]
#   else:
#     return "out is not 4 characters"

# print(make_out("[[]]", "Vanessa"))

# def extra_end(str):
#  return str[-2:] * 3

# print(extra_end("vanessa"))

# def first_two(str):
#  if len(str) % 2 == 0:
#   half = len(str) / 2
#   return str[:int(half)]
#  else:
#   return "string is not even"

# print(first_two("kubanacan"))

# def first_two(str):
#  if len(str) >= 2:
#   return str[:1]+str[-1:]
#  else:
#   return "too small string"

# print(first_two("Herry"))

# def missing_char(str):
#   c = str[1:-1]
#   return c

# print(missing_char("Vanessa"))

# def combo_string(a, b):
#   if len(a) < len(b):
#     return a+b+a
#   else:
#     return b+a+b
# print(combo_string("Vanessa", "Everton"))

# def missing_char(a, b):
#   return a[1:]+b[1:]
# print(missing_char("Hello","World"))

# def left2(str):

#  first2 = str[:2]
#  str2 = str[2:]
#  return str2+first2
# print(left2("Hello"))

# def cigar_party(cigars, is_weekend):
#   if is_weekend == False and cigars >= 40 and cigars <= 60:
#       return True
#   elif is_weekend == True and cigars >= 40:
#    return True
#   else:
#     return False
# print(cigar_party(40, True))

# def date_fashion(you, date):
#   if you <= 2 or date <= 2:
#    return 0
#   elif you >= 8 or date >= 8:
#    return 2
#   else:
#    return 1
# print(date_fashion(2, 8))

# def squirrel_play(temp, is_summer):
#  if is_summer == True and temp >= 60 and temp <= 100:
#   return True
#  elif is_summer == False and temp >= 60 and temp <= 90:
#   return True
#  else:
#   return False
# print(squirrel_play(100, False))

# You are driving a little too fast, and a police officer stops you. 
# Write code to compute the result, encoded as an int value: 0=no ticket, 1=small ticket, 2=big ticket. 
# If speed is 60 or less, the result is 0. If speed is between 61 and 80 inclusive, the result is 1. 
# If speed is 81 or more, the result is 2. Unless it is your birthday -- on that day, your speed can be 5 higher in all cases.
# def caught_speeding(speed, is_birthday):
#  if is_birthday and speed is >
#   return

num2 = 2.0
print(num2, 'is of type', type(num2))