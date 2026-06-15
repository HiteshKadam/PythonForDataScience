#Control Flow
print(True)
print(False)
print(type(True))
print(bool(123))
print(bool("Stre"))
print(bool())
print(bool(0))
print(bool(""))
print(bool(None))


email = ""
phone = 12345234534
username = ""

print(any([phone,email,username]))
print(all([email,phone,username]))

print(isinstance(phone,int))

#is age between 18 and 30
age = 20
print(18 <= age <=30)# ))

# Operators > < <= >= !=

# Logical operators and or not

x = 5
y =9
print(x > 5 or y > 5 )

is_logged_in = True
is_guest = False
is_banned = True

print((is_logged_in or is_guest) and not is_banned)

# membership in / not in

print("i" in "Hitesh")
print(3 not in [1,2,3])

# identity operator is / is not
x = [1,2,3]
y = [2,3]
print(x is y)
print(x == y)

a = [1,2,3]
b = [1,2,3]
print(a is b)

email = None
print(email is not None and email != "")

#Challenge
#q1
name = "Hitesh"
age = 26
banned = "Banned"
verified = True
print(name != "" and age >= 18)

#q2
password = "adwdq awd"
print(len(password) >= 8 and " " not in password)
#loops

for i in range(1,6):
    print(f"Round: {i}")

scores = [80,50,90,75]
total = 0
for score in scores:
    total += score
    print("Current Total: ", total)
print("Final Total: ", total)

#Challenge 1

for i in range(1,11):
    print(f"7 x 1 = {i*7}")

#Challenge 2

for i in range(1,7):
    print("*"*i,end="\n")

names = ['john','jacob','','kumar']

for name in names:
    if name == '':
        print("Name is empty")
        #break/continue/pass
    print("Name is:", name)

names = ['Kamara', 'Tuba', 'Maria','Mounika']

for name in names:
    if name is None:
        print("Name is empty")
        break
else:
    print("All names are available")

files = ["data1.csv", "data2.csv", "data3.pdf"]

for file in files:
    if not file.endswith(".csv"):
        print("Skipping file: " + file)
        break
else:
    print("All files are CSV!")


#Challenge 1
file_list = ['report.csv','data.xlsx','summary.docx','report.csv','data.csv']

for file in file_list:
    if file_list.count(file) > 1:
        print("Duplicate Found")
        break
else:
    print("All Files are unique!")


#nested loops
years = [2026 , 2027]
month = ['Jan', 'Feb']
days = range(1,29)
for y in years:
    for m in month:
        for d in days:
            print(f'report_{y}_{m}_{d}.csv')

# While Loops
i = 0
while i < 4:
    print(i)
    i+=1

input_u = "no"
while input_u != "yes":
    input_u = str(input("Do you agree?"))
while True:
    answer = input("Do you agree (Yes/No): ")
    if answer == "Yes":
        break
print("Thank you for your time!")
count = 0
while count < 3:
    answer = input("Do you agree? (yes/no:)")
    count+=1
    if answer == "yes":
        print("Glad we are on same Page")
        break
else:
    print("3 Strikes You are Out!")

#q3
email = "ajwdnawkdn@gmail.com"
print(email != "" and "@" in email and email.endswith(".com"))

#q4
print(isinstance(name,str) and name is not None and len(name) >  5)

#q5
print(name in ["admin","moderator"] and (banned != "Banned" or verified == True))