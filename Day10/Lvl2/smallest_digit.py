n=int(input("Enter a number: "))
smallest=9
while n>0:
    digit=n%10
    if digit<smallest:
        smallest=digit
    else:
        pass
    n=n//10
print(smallest)