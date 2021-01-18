def merge_the_tools(string, k):
    arr = []
    count = 0
    s = ''
    for i in string:
        count += 1
        if count%k == 0:
            s += i
            arr.append(s)
            count = 0
            s = ''
        else:
            s += i
    
    # print(arr)
    
    for each_sub in arr:
        unique = ''
        for letter in each_sub:
            if letter not in unique:
                unique += letter
        print(unique)
        
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
