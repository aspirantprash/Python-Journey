n=int(input("Enter a Number: "))
count=0
for i in range(1,n+1):
    if n%i==0:
        count+=1
    else:
        pass
if count==2:
    print("Prime")
else:
    print("Not")
