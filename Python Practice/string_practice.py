# String
"""
- Types
- Math
- Transformations
- Cleaning
- Search
- Validation
"""

#Types

name = "Hitesh"
print(type(name))

age = 26
print(type(age))

print("Your age is:"+str(age))


#Math

password = " 123aawdAWDW3"
print(len(password))

if len(password) < 8:
    print("Your password is too short")


text = """
Python is easy to learn.
Python is powerful
Many learn python
"""

print(text.count("Python"))


# Transformations
price = "1234,56"
print(price.replace(",","."))

phone = "176-1234-56"
print(phone.replace("-","/"))

print(phone.replace("-",""))

price = "$1,299.99"
print(price.replace("$","").replace(",",""))


task_text = "+49 (176) 123-4567"
print(task_text.replace("+","00")
      .replace(" ","")
      .replace("(","")
      .replace(")","")
      .replace("-",""))


first_name = "Hitesh"
last_name = "Kadam"

last_name =  first_name + " " + last_name
print(last_name)

folder = "C:/Users/Hitesh"
file = "repost.csv"

full_file_path = folder + "/" + file
print(full_file_path)

name = "Hitesh"
age = 26
is_student = False

print("My name is " + name + ", I am " + str(age) + " years old, and student status is " + str(is_student) + ".")
print(f"My name is {name}, I am {age} years old, and student status is {is_student}.")


print(f"2 + 3 = {2+3}")


stamp = "2026-09-20"
print(stamp.split("-"))

csv_file = "1234,Max,USA,2000-02-19,M"
print(csv_file.split(","))


print("ha" * 3)
print("="*20)

### Extraction
text = "Python"

print(text[-6])
print(text[-1])

print(stamp[0:4])
print(stamp[:4])


#Cleaning
# --> White Spaces
text = " Engine "
print(text.lstrip())
print(text.rstrip())
print(text.strip())

# --> Case Conversion
print(text.lower())
print(text.upper())

#Challenge
practice_text = "968-Maria, ( D@t@ Engineer ) ;; 27y  "

cleaned_string = (practice_text.replace("968-","")
                  .replace("(","")
                  .replace(")","")
                  .replace(";;",",")
                  .replace("@","a")
                  .rstrip("y  ").split(","))
print(f"name: {cleaned_string[0].lower()} | role: {cleaned_string[1].lower().strip()} | age: {cleaned_string[2].strip()}")


#search
phone = "+49-16-12345"
print(phone.startswith("+49"))

email = "dkadam@gmail.com"
print(email.endswith("gmail.com"))

print("@" in email)

print(phone.find("-"))

#Validation
country = "USA"
print(country.isalpha())

print("12903-12321-12".isnumeric())