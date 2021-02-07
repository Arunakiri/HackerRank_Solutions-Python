# Sort the array only once and try to add and remove the respective elements to that sorted array.
# Sorting each time will increase time complexity and reduce the code efficiency.
# Note: bisect and bisect_left have Runtime difference
# similarly for insort and insort_left - Use insort_left/bisect_left
# remove() attribute also time consuming. Use del function.

from bisect import bisect_left, insort_left

n, d = map(int, input().split())
expenditure = list(map(int, input().split()))

notifications = 0

arr = sorted(expenditure[:d])

for i in range(d,n):
  if d%2 == 1:
      median = 2*arr[d//2]
  else:
      median = (arr[d//2] + arr[d//2-1])
        
  if expenditure[i] >= median(): 
      notifications += 1
  
  del arr[bisect_left(arr, expenditure[i-d])]
  insort_left(arr, expenditure[i])

print(notifications)
