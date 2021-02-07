# Swap the adjacent elements if not in increasing order
# Carry out the swap loop n times where n is the length of the array

def countSwaps(a):
    count = 0
    for i in range(len(a)):
        for j in range(len(a)-1):
            if a[j] > a[j+1]:
                t = a[j]
                a[j] = a[j+1]
                a[j+1] = t
                count += 1
    print('Array is sorted in', str(count), 'swaps.')
    print('First Element:', a[0])
    print('Last Element:', a[-1])

if __name__ == '__main__':
    n = int(input())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
