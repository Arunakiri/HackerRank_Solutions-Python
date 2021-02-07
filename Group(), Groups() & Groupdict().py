import re

string = input()

m = re.search(r'([0-9a-zA-Z])\1', string)

if m:
    print(m.group(1))
else:
    print('-1')
    
