def check(num):
    org=num
    result=0
    result_bro=0

    while num>0:
        last_digit=num%10
        result=result*10+last_digit
        num=num//10
    if result==org:
        print("Palindrom")
    else:
        print("Not")
result_bro=check(45564)