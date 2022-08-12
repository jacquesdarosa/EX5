# do exercise here
# upload to github for portfolio
# thank me later when your git graph is as green as the python money u gonna earn


'''# task 1

def sum_thrice(x, y, z):
     sum = x + y + z
     if x == y == z:
      sum = sum * 3
     return sum
print(sum_thrice(3, 4, 5))
print(sum_thrice(5 ,5, 5))

# task 2

n1= int(input("enter 1st number="))
n2= int(input("enter 2nd number="))

if n1 > n2:
    print(2*(n1 -n2))
   


else:
    print(abs(n1-n2))'''

'''# task 3

num = int(input("enter a number="))
mod = num % 2

if mod > 0:
    print("This is an odd number")
else:
    print("This an even number")'''

# task 4
# import math library

'''import math
print(math.pi)

from math import pi
r = float(input("Input the radius of the circle="))
area = math.pi * r *r 
print ("Area of a circle = %.2f" %area)'''

# task 5

import random
target_num, guess_num = random.randint(1, 10), 0
while target_num != guess_num: 
    guess_num = int(input("Guess a number from 1 to 10 till you get it right="))
print ("Well guessed")


