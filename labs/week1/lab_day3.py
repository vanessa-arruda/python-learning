#Given a list of integers, return True if the sequence of numbers 1, 2, 3 appears in the list somewhere.

def listCheck(my_list):
    for i in range(len(my_list)-2):
        if my_list[i] == 1 and my_list[i+1] == 2 and my_list[i+2] == 3:
            return True
        else:
            return False

listCheck([1,2,0,1,2,3])

#Given a string, return a new string made of every other character starting with the first, so "Hello" yields "Hlo".

def changeStr(str):
    if len(str) <= 1:
        return str
    else:
        
changeStr("V")