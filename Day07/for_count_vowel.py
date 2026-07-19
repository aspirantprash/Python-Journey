count=0
word = input("Enter a string: ")
for ch in word:
    if ch in 'aeiouAEIOU':
        count=count+1
print("The number of vowels in the string is:", count)