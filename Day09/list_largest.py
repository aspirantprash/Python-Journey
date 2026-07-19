numbers = [12, 45, 7, 25, 23, 56]
largest=numbers[0]
for num in numbers:
    if num > largest:
        largest = num
    else:
        pass
print (largest)  