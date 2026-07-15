n=int(input("Enter a Number: "))
largest=0
while n>0:
    digit=n%10
    if digit>largest:
        largest=digit
    else:
        pass
    n=n//10
print(largest)