def word(string):
    count=0
    for ch in string:

        if ch=="A" or ch=="a" or ch=="E" or ch=="e" or ch=="I" or ch=="i" or ch=="O" or ch=="o" or ch=="U"or ch=="u":
            count=count+1
        else:
            pass
    return count
count=word("Hey, I am an Aspirant broh!")
print (count)