def count_consonant(text):
    count=0
    for ch in text.lower():
        if ch in "aeiou":
            pass
        else:
            count+=1
    return count
print(count_consonant("Introduction: Hey, I am Prashant and I am Future developer."))