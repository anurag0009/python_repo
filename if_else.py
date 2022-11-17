# if_else_Statement
name = input("Enter the code : ")
if name == "Anurag":
    print("ypu will get discount of 10%")
    paid_amount = 15000 - 15000 * .10
    print("you get a diacounr of :", paid_amount)
else :
    print("Enter valid Code")

# if else _elif

course = input("Enter the course name : ")

if course == "DSA":
    print("you have to check the link on ineuron")
elif course == "Data Science":
    print("you enter on the correct portal")
elif course == 'analytics':
    print("go check on youtube")
else:
    print("find the course by yourself")