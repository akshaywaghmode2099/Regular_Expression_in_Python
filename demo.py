import re

txt=input("Enter string")

#l=re.findall("[a-z]{4,}",txt) #minimum 4 character

#l=re.findall("^[a-z][a-z]{2}[a-z]$",txt)#only 4 characters

l=re.findall("he...o",txt)
print(l)
if l:
    print("pattern match")
else:
    print("pattern not match")
