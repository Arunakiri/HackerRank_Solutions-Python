import re

n = int(input())

pattern = r'(?<=.)#{1}[a-fA-F0-9]{3,6}'
for _ in range(n):
    match = re.findall(pattern, input())
    for m in match:
        print(m)
