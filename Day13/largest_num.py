def num(a,b,c):
    result=""
    if a>b and a>c:
        result=a
    elif b>a and b>c:
        result=b
    else:
        result=c
    return result
result=num(145,57,77)
print(f"Largest number is: {result}")