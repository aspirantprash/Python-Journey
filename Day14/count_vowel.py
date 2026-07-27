""" def count_vowel(word):
    count=0
    for ch in word:
        if ch=="A" or ch=="a" or ch=="E" or ch=="e" or ch=="I" or ch=="i" or ch=="O" or ch=="o" or ch=="U" or ch=="u":
            count+=1
        else:
            pass
    return count
print(count_vowel("Myself Prashant Sharma Nice to meet U."))
"""
def count_vowel(text):
    count=0
    for ch in text.lower():
        if ch in "aeiou":
            count+=1
    return count
print(count_vowel("Myself Prashant Sharma Nice to meet U."))
