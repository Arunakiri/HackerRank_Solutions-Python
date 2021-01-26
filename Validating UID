import re

n = int(input())
for _ in range(n):
    s = input()
    if len(s) == 10 and s.isalnum():
        if bool(re.search(r'(.*[A-Z]){2,}', s)) and bool(re.search(r'(.*[0-9]){3,}', s)):
            if bool(re.search(r'.*(.).*\1', s)):
                print('Invalid')
            else:
                print('Valid')
        else:
            print('Invalid')
    else:
        print('Invalid')
