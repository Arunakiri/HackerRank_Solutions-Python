if __name__ == '__main__':
    arr = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        arr.append([name,score])
        
    arr = sorted(arr, key=lambda x:x[1])
    
    for i in range(1, len(arr)):
        if arr[i][1] > arr[0][1]:
            second = arr[i][1]
            break
        
    name = []
    for i in range(1, len(arr)):
        if arr[i][1] > second:
            break
        if arr[i][1] == second:
            name.append(arr[i][0])

for i in sorted(name):
    print(i)
