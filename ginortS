string = input()

l, u, o, e = '', '', '', ''

for i in string:
    if i.islower():
        l += i
    elif i.isupper():
        u += i
    elif i.isdigit():
        if int(i)%2 != 0:
            o += i
        else:
            e += i
result = ''.join(sorted(l)+sorted(u)+sorted(o)+sorted(e))
print(result)
