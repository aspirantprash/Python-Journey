unit=int(input("Enter the number of units consumed: "))
rate1=5
rate2=7
rate3=10

if 0<= unit <=100:
    bill=unit*rate1
    print("Your electricity bill is: ",bill,"Rs")
elif 101<= unit <=200:
    bill=unit*rate2
    print("Your electricity bill is: ",bill,"Rs")
else:
    bill=unit*rate3
    print("Your electricity bill is: ",bill,"Rs") 