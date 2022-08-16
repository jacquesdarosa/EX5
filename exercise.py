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

'''# task 5

import random
target_num, guess_num = random.randint(1, 10), 0
while target_num != guess_num: 
    guess_num = int(input("Guess a number from 1 to 10 till you get it right="))
print ("Well guessed")'''


'''# task 6

Celsius_1 = float(input("Temperature value in Celsius="))
Fahrenheit_1 = (Celsius_1 * 1.8) + 32
print("The %.2f degree Celsius is equal to: %.2f Fahrenheit"
    %(Celsius_1, Fahrenheit_1))'''

# task 7 - pattern

n=5
for i in range(n):
    for j in range(i):
        print ('* ', end="")
    print('')

for i in range(n,0,-1):
    for j in range(i):
        print('* ', end="")
    print('')
	

# task 8 Fibonnaci series

x,y = 0,1

while y<50:
    print(y)
    x,y = y, x+y







