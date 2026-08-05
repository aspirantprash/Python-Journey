name=str(input("Enter your Name: "))

math=int(input("Enter Math Marks: "))
phy=int(input("Enter Physics Marks: "))
chem=int(input("Enter Chemistry Marks: "))
eng=int(input("Enter English Marks: "))
hindi=int(input("Enter Hindi Marks: "))

total=(math+phy+chem+eng+hindi)

perc=total/5

if perc >=95 and perc <100:
    grade="A+"
elif perc >= 90:
    grade="A"
elif perc >= 80:
    grade="B"
elif perc >= 65:
    grade="C"
elif perc >= 55:
    grade="D"
elif perc >= 30:
    grade="E"
else:
    grade="Fail"
if perc>=30:
    Division="Pass"
else:
    Division="Fail"


print(f"Total Marks: {total}\n Percentage: {perc}\n Grade: {grade}\n {Division}")