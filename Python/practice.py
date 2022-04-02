# Write a function that returns the lesser of two given numbers if both numbers are even, 
# but returns the greater if one or both numbers are odd

def lesserOfTwoEvens(a,b):
    if a % 2 == 0 and b % 2 == 0:
        if a<b:
            return a
        return b
    else:
        if a > b:
            return a
        return b

print(lesserOfTwoEvens(2,4))
print(lesserOfTwoEvens(10,30))



#  Write a function takes a two-word string and 
# returns True if both words begin with same letter
def animalCracker(string):
    x = string.split()
    if x[0][0] == x[1][0]:
        return True
    return False

print(animalCracker('Levelheaded Llama'))
print(animalCracker('Crazy Kangaroo'))



# Given two integers, return True if the sum of the integers is 20 
# or if one of the integers is 20. If not, return False

def makesTwenty(n1,n2):
    if n1 == 20 or n2 == 20:
        return True
    elif n1 + n2 == 20:
        return True
    return False

print(makesTwenty(20,10))
print(makesTwenty(12,8))
print(makesTwenty(2,3))



# Write a function that capitalizes the first and fourth letters of a name..

def caps(string):
    g = ''
    for i,j in enumerate(string):
        if i == 0 or i == 3:
            g += j.upper()
        else:
            g += j
    return g

print(caps('macdonald'))



# Given a sentence, return a sentence with the words reversed
def masterYoda(st):
    x = st.split()
    return " ".join(x[::-1])

print(masterYoda('I am Home'))
print(masterYoda('We are ready'))



# Given an integer n, return True if n is within 10 of either 100 or 200

def almostThere(n):
    if n in range(90,111) or n in range(190, 211):
        return True
    return False

print(almostThere(190))
print(almostThere(109))
print(almostThere(150))
print(almostThere(210))
print(almostThere(179))


#Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.

    for i in range(0, len(nums)):
        if(i+1 < len(nums)):
            if(nums[i] == 3 and nums[i+1] == 3):
                return True
    return False

has33([3,3,1,2,4])
- True
has33([1,3,3])
- True
has33([1,3,1,3])
- False
has33([3,1,3])
- False
