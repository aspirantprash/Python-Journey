n=int(input("Enter a number: "))
i=1
total=0
while i<=n:
    if i%2==0:
        total=total+i
    i+=1
print("The sum of even numbers from 1 to", n, "is:", total)