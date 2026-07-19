base=int(input("Enter the base number: "))
power=int(input("Enter the power number: "))
result=1
i=1
while i<=power:
    result=result*base
    i+=1
print(result)