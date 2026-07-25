def list(*numbers):
    total=0
    for i in numbers:
        total=total+i
    return total
total=(list(10,1,4,5))
print(total)