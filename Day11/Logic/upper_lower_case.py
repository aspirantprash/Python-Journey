str="PrasHant"
upper=0
lower=0
for ch in str:
    if "A" <= ch <= "Z":
        upper+=1
    elif "a" <= ch <= "z":
        lower+=1
    else:
        pass
print(upper)
print(lower)