name=str(input("Enter your Name: "))

math=int(input("Enter Math Marks: "))
phy=int(input("Enter Physics Marks: "))
chem=int(input("Enter Chemistry Marks: "))
eng=int(input("Enter English Marks: "))
hindi=int(input("Enter Hindi Marks: "))

total = (math+phy+chem+eng+hindi)
percentage = total / 5

print("\n--------- RESULT ---------")

print(name)

print("Total Marks: ",total)

print("Percentage: ",percentage)

if total>=150:
    print ("Status: pass")
else:
    print("Status: Fail")

if 90 <= percentage <= 100:
    grade="A+"
elif percentage >= 80:
    grade="A"
elif percentage >= 70:
    grade="B"
elif percentage >= 60:
    grade="C"
elif percentage >= 50:
    grade="D"
elif percentage >= 33:
    grade="E"
else:
    pass
print("Grade=",grade)