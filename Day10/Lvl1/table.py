n=int(input("Enter a Number: "))
print("The Multiplication Table of",n,"are:")
for i in range(1,11):
    table=n*i
    print(f"{n} * {i} = {table}")