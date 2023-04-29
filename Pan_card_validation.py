'''Pan card validation
pan card ten characters
first 5 upper case letters
next 4 digit last upper case character'''

import re
txt=input("Enter pan no")
x=re.search("\A[A-Z]{5}[0-9]{4}[A-Z]{1}$",txt)
if x:
    print("valid pan card no ")
else:
    print("invalid pan card no")
