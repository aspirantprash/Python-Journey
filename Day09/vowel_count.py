string=str(input('Enter String : '))
count=0
for str in string:
    if str == "A" or str=="a" or str=="E" or str=="e" or str=="I" or str=="i" or str=="O" or str=="o" or str=="u" or str=="U":
        count=count+1
    else:
        pass
print(count)