text=input("Enter your sentence: ")
count=0
for ch in text.lower():
    if ch in "aeiou":
        pass
    else:
        count+=1
print(f"Total consonant= {count}")