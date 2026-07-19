string="prarp"
rev=""
for str in range(len(string)-1,-1,-1):
    rev=rev+string[str]
if rev==string:
    print("Palindrom")
else:
    print("Not Palindrom")