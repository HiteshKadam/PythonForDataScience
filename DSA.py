#4 datatypes
"""
1: list - common  [-,-,-]
2: tuple - No Changes   (-,-,-,-)
3: set - unique {-,-,-,-}
4: dict - key-value {-:-,-:-,}
"""

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
