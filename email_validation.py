#email id validation

import re
txt=input("Enter email ")
x=re.search("^[a-z]+[a-z0-9_]*@[a-z0-9]+[.][a-z]{2,3}$",txt)
if x:
    print("valid email ")
else:
    print("invalid")
