#Write RE for mobile no checing


import re
mob=input("Enter mob no ")

x=re.search('^[7-9][0-9]{8}[0-9]$',mob)
if x:
    print("valid Mob No ")
else:
    print("Invalid mob no ")


