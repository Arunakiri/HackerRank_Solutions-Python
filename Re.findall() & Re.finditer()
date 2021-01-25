import re

string = input()

m = re.findall(r'(?<=[^aeiou])([aeiou]{2,})(?=[^aeiou])', string, re.IGNORECASE)

if m:
    for i in m:
        print(i)
else:
    print('-1')
