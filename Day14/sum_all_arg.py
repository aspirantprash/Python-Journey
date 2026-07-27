def add(*numbers):
    total=0

    for num in numbers: 
        total=total+num
    return total #ab total calculate ho kar return fn total return kr dega

print(add(22,45,67,89,55))