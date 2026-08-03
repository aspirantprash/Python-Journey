#Question: Ek list banao [5, 2, 8, 1, 9, 3] — ise sort karo, reverse karo, max aur min nikalo

nums= [5, 2, 8, 1, 9, 3] 

#Ascending order
nums.sort()
print(f"Ascending order: {nums}")

#reverse
nums.sort(reverse = True)
print(f"Reverse order: {nums}")

#Maximum
print(f"Maximum Number: {max(nums)}")

#Minimum
print(f"Minium Number: {min(nums)}")
