def function(s):
    temp = s[0]
    count = 0
    
    for letter in s:
        
        if letter == temp:
            count += 1
        else:
            print('({0}, {1})'.format(count, temp), end=' ')
            temp = letter
            count = 1
    print('({0}, {1})'.format(count, temp))
     
s = input()
function(s)
