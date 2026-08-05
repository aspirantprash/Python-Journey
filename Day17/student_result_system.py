name=str(input("Enter your Name: "))
# 1. Input lene ka function
def get_marks():
    maths=int(input("Math: "))
    phy=int(input("Physics: "))
    eng=int(input("English: "))
    hindi=int(input("Hindi: "))
    chem=int(input("Chemistry: "))

    return maths,phy,chem,eng,hindi
maths,phy,chem,eng,hindi = get_marks()

# 2. Total aur Percentage calculate karne ka function
def calculate_result(maths,phy,chem,eng,hindi):
    total=maths+phy+chem+eng+hindi
    perc=total/5
    return total,perc
total, perc = calculate_result(maths,phy,chem,eng,hindi)

# 3. Grade nikalne ka function
def get_grade(perc):
    if 95 <= perc <= 100:
        grade="A+"
    elif perc >= 90:
        grade="A"
    elif perc >= 80:
        grade="B"
    elif perc >= 65:
        grade="C"
    elif perc >= 55:
        grade="D"
    elif perc >= 33:
        grade="E"
    else:
        grade="Fail"

    return grade
grade=get_grade(perc)
    

# 4. Pass/Fail check karne ka function
def get_division(perc):
    if perc >= 33:
        division="Pass"
    else:
        division="Fail"
    return division

division=get_division(perc)

# 5. Final result print karne ka function
def display_result(name,total,perc,grade,division):
    print(f"Name: {name}")
    print(f"Total Marks: {total}")
    print(f"Percentage: {perc}")
    print(f"Grade: {grade}")
    print(f"Division: {division}")
result=display_result(name,total,perc,grade,division)