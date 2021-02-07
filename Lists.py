if __name__ == '__main__':
    N = int(input())
    arr = []
    for i in range(N):
        i = input().split()
        
        if i[0].lower() == 'insert':
            arr.insert(int(i[1]), int(i[2]))
        elif i[0].lower() == 'print':
            print(arr)
        elif i[0].lower() == 'remove':
            arr.remove(int(i[1]))
        elif i[0].lower() == 'append':
            arr.append(int(i[1]))
        elif i[0].lower() == 'pop':
            arr.pop()
        elif i[0].lower() == 'sort':
            arr.sort()
        elif i[0].lower() == 'reverse':
            arr.reverse()
