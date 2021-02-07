import re

n = int(input())

for _ in range(n):
    string = input()
    m = re.match(r'^[+-]?[0-9]*\.[0-9]+$',string)

    if m:
        print(True)
    else:
        print(False)
