def check(num):

    result=""
    if num % 2 == 0:
        result="Even"
    else:
        result="Odd"
    return(result)

result=check(14)
print(result)