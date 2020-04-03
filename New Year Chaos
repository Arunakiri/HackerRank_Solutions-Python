# Try counting who got the bribes instead of who moved in front of the array.
# Find how many higher values before the selected value will provide the output.
# Note: max(e-1, 0); 0 if for positive entries incase any negative value arrives.


def minimumBribes(q):
    arr = [i-1 for i in q]
    bribe = 0
    
    for i, e in enumerate(arr): 
        if e-i > 2:
          return "Too chaotic"
        for val in arr[max(e-1, 0):i]:
            if val > e:
                bribe += 1
    
    return bribe

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        print(minimumBribes(q))
