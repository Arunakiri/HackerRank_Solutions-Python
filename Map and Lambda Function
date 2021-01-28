cube = lambda x: x**3

def fibonacci(n):
    arr = [0, 1]
    for i in range(2, n):
        arr.append(arr[i-2]+arr[i-1])
    
    return arr[0:n]

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
