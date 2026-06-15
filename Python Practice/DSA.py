#4 datatypes
"""
1: list - common  [-,-,-]
2: tuple - No Changes   (-,-,-,-)
3: set - unique {-,-,-,-}
4: dict - key-value {-:-,-:-,}
"""
import copy

# Create
empty = list()
print(empty)

letters = list('Python')
print(letters)

number = list(range(10))
print(number)

matrix = [
   ['a', 'b', 'c'],
   ['d', 'e', 'f'],
   ['g', 'h', 'i']]
print(matrix)
print(matrix)

mixedmatrix = [
   ['a', 'b', 'c'],
   [1,2,3]]
print(mixedmatrix)

# Read and Access
print(number[9])
print(number[0:5])
print(number[-1:-6:-1])

print(matrix[1])
print(matrix[1][1])

#Unpacking
person = ['Maria', 29 , 'Data Engineer', 'Spain']
name, age, role, country = person
name, *details, country = person
name, *_, country = person
print(role)
print(details)
print(_)


#Explore & Analyze
numbers = [1,5,2,4,3]
print(f'Max: {max(numbers)}')
print(f'Min: {min(numbers)}')
print(f'Sum: {sum(numbers)}')
print(f'Length: {len(numbers)}')

print("All: ",all(numbers))
print("All: ",all([1,0,2]))
print("All: ",all(['a','','c']))
print("All: ",all(['a','b','c']))


print("All: ",any(numbers))
print("All: ",any([1,0,2]))
print("All: ",any(['a','','c']))
print("All: ",any([0,0,0]))

print("Count: ",numbers.count(5))
print("Index: ",numbers.index(5))

#Analysis & Checks
list1 = [1,5,5,4,3]
list2 = [1,5,5,4]
print(8 not in numbers)
print(list1 is list2)

#Changing List
# Add items
print(letters)
letters.append('v')
letters.insert(0,'z')
print(letters)

#remove items
# letters.clear()
letters.remove('z')
letters.pop(0)
print(letters)

#update items
letters[2] = 'l'
print(letters)

#sort
print(numbers)
# numbers.sort(reverse=True)
# print(sorted(numbers, reverse=False))
# print(numbers)

# numbers.reverse()
print(list(reversed(numbers)))


# Copy
original = ['a','b','c']
cpy_list = original

cpy_list_1 = original.copy()

cpy_list_2 = copy.deepcopy(original)


#Combining
comb = letters + numbers
print(comb)
comb1 = list(zip(letters, numbers))
print(comb1)

# Iterators
print(list(enumerate(letters, start=1)))


for index, value in enumerate(letters):
   print(index, value)



for l, n in zip(letters, numbers):
   print(n, l)


letters = ['a','','c',None, False]
print(list(filter(None, letters)))

items = ['sql','123','pythin','42']
print(list(filter(str.isalpha, items)))

#Lambda
multiple = lambda x: x*2
print(multiple(5))

add = lambda x,y : x + y
print(add(3,4))

check = lambda i: i in "python"
print(check("n"))

prices = ['$12.50','$9.99','$100.00']
p = '$12.50'

print(list(map(lambda p : float(p.replace('$','')),prices)))

prices = [120,30,300,80]
print(list(filter(lambda p : p>=100, prices)))

domains = ['www.google.com','localhost','openai.com','WWW.DATAWITHHITESH.COM']

cleaned = [
   d.lower().replace('www.','')
   for d in domains
   if '.' in d
]
print(cleaned)
