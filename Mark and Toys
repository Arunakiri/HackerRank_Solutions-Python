# Sort the array and add the elements from the start one by one 
# untill the sum is greater than or equal to the amount in hand


def maximumToys(prices, k):
    arr = sorted(prices)
    toys, val = 0, 0
    for i in arr:
        val += i
        if val < k:    
            toys += 1
    
    return toys


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    prices = list(map(int, input().rstrip().split()))

    result = maximumToys(prices, k)

    fptr.write(str(result) + '\n')

    fptr.close()
