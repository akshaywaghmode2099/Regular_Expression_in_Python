#Adhar card no Regular Expression

import re
txt=input("Enter adhar no")
x=re.findall("^[2-9]{1}\d{3} [0-9]{4} [0-9]{4}$",txt)
if x:
    print("valid Adhar NO")
else:
    print("invalid")
