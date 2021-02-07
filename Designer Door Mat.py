h, w = map(int, input().split())

# Top
for i in range(1, h, 2):
    print(('.|.'*i).center(w, '-'))

print('WELCOME'.center(w, '-'))

# Bottom
for i in range(h-2, -1, -2):
    print(('.|.'*i).center(w, '-'))
