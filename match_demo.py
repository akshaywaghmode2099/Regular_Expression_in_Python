import re
txt=input("Enter string ")
x=re.match('[a-z]',txt)
if x:
    print("match")
else:
    print("not match")
