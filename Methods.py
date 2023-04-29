import re
txt=input("Enter String ")
'''l=re.findall('[a-zA-Z]+[A-Za-z0-9]*[0-9]$',txt)
print(l)
l=re.search('[a-zA-Z]+[A-Za-z0-9]*[0-9]$',txt)
print(l)
'''

l=re.findall('[0-9]',txt)
print(l)
l=re.search('[0-9]',txt)
print(l)
