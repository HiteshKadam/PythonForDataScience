#types
import math
import random

x = 43
y = 5.7
z = 2 + 3j

print(type(x))
print(type(y))
print(type(z))

x = int("24")
x = 3.14
print(int(x))

#Operators

# + - * / // % **

#rounding numbers
price = 35.234
print(math.ceil(price))
print(math.floor(price))
print(round(price))
print(math.trunc(price))

#Random
print(random.random())
print(random.randint(1, 6))


#Validation
x= 7.0
print(x.is_integer())

y= 7.1
print(y.is_integer())

x = 70.4
print(isinstance(x,int))


challenge_numeric = random.randint(1,100)
print(challenge_numeric % 2 == 0)