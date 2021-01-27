import re

string, substring = input(), input()

pattern = re.compile(substring)
match = pattern.search(string)

if not match:
    print('(-1, -1)')

while match:
    print("(%s, %s)" % (match.start(), match.end()-1))
    match = pattern.search(string, match.start()+1)
