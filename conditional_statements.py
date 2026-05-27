#Conditional Statement

def check_even(num):
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")


check_even(10)
submitted_project = True

score = 10
if score >= 90:
    print("A")
elif score>= 80:
    print("B")
else:
    print("F")

if score>=90:
    print("A")
    if submitted_project:
        print("A+")
    else:
        print("A")
elif score>=80:
    print("B")
else:
    print("F")

if score>=90 and submitted_project:
    print("A+")
elif score>=90:
    print("A")
elif score>=80:
    print("B")
elif score>=70:
    print("C")
elif score>=60 or submitted_project:
    print("D")
else:
    print("F")


print("A" if score >= 90 else "B")



country = "India"
match score:
    case "India": print("IN")
    case "Egypt": print("EG")
    case "Germany": print("DE")
    case "United States": print("US")
    case _: print("Unknown Country")

# Challenge 1

mailin = "hitesh.kadam@tifr.res.in"
def check_mail(mail):
    if mail == "" or mail is None:
        return False
    if "." not in mail and "@" not in mail:
        return False
    if not(mail.endswith((".com",".edu",".org",".in"))):
        return False
    if len(mail) > 254:
        return False
    if mail.count("@") != 1:
        return False
    if not(mail[0].isalnum() and mail[-1].isalnum()):
        return False
    return True

print("Email Valid" if check_mail(mailin) else "Email Invalid")


#Challenge 2
password = "KdkwalWA"

def check_password(passw: str):
    if passw == "" or passw is None:
        return False
    if len(passw) < 8:
        return False
    if not any(char.isupper() for char in passw) and not any(char.islower() for char in passw):
        return False
    if passw == mailin and " " in passw:
        return False
    if not(passw[0].isalnum() and passw[-1].isalnum()):
        return False
    return True

print("Password Valid" if check_password(password) else "Password Invalid")
