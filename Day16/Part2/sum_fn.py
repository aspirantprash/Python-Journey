def sum_all(*number):
    sum=0
    for num in number:
        sum=sum+num
    return sum
sum = sum_all(1,2,3,4,5,6,7,8,9,10)
print("Sum: ",sum)
