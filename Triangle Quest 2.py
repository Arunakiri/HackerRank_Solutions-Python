# Using String
for i in range(1,int(input())+1): 
    print(''.join([str(a) for a in range(1, i) if i>1])+str(i)+''.join([str(b) for b in range(i-1, 0, -1) if i>1]))

# Formula
for i in range(1,int(input())+1):
    print(((10**i-1)//9)**2)

'''
1*1         - 1
11*11       - 121
111*111     - 12321
1111*1111   - 1234321
11111*11111 - 123454321
'''
