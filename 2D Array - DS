# Use 2 for loops to move along the matrix elements.
# Since, there will be negative results, use max() to get the result.

def hourglassSum(arr):
    val = []

    for i in range(len(arr)-2):
        for j in range(len(arr)-2):
            total = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1] + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
            val.append(total)
    
    return max(val)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')
    fptr.close()
