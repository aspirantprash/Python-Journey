n=int(input("Enter a number: "))

count=1

even_count=0
odd_count=0

while count<=n:

    if count % 2==0:
        even_count=even_count+1
    else:
        odd_count=odd_count+1

    count=count+1

print("Even count:", even_count)
print("Odd count:", odd_count)
    