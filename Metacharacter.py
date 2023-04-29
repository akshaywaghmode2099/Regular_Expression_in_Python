import re
txt=input("Enter pan no")
x=re.findall("\d\Z",txt)
print(x)
if x:
    print("found")
else:
    print("not found")
