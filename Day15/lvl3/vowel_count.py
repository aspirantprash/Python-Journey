text="A brave coder zealously queries every system, yet finds joy in debugging, tweaking, optimizing, navigating, mastering — finally, victory!"
count=0
for ch in text.lower():
    if ch in "aeiou":
        count+=1
print(count)