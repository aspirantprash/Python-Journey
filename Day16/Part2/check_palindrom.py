text=str(input("Enter your text: "))
org=text
rev=text[::-1]
if org==rev:
    print("True")
else:
    print("False")