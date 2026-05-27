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
