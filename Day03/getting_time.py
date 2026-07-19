time=int(input("Enter the time in Hour format: "))
if 0 <= time <= 24:
    if 0 <= time < 12:
        print("Good Morning")
    elif 12 <= time < 16:
        print("Good Afternoon")
    elif 16 <= time < 20:
        print("Good Evening")
    else :
        print("Good Night") 
else:
    print("Not Valid Time")   
