string=str(input("Enter a String: "))
rev=""
for str in range(len(string)-1,-1,-1):
    rev=rev+string[str]
print(rev)