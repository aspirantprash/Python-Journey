def reverse(num):
    rev=0
    while num>0:
        last_digit=num%10
        rev=rev*10+last_digit
        num=num//10
    return rev
rev=(reverse(5678))
print(rev)