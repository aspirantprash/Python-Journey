def find(*numbers):
    largest=numbers[0] #largest num is first number

    for num in numbers: 
        if num >= largest: #hr num check hoga agr hain to update....
            largest=num
    return largest

print(find(12,13,14,15))