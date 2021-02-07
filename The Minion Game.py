def minion_game(string):
    vowels = 'AEIOU'
    Stuart, Kevin = 0, 0
    for i in range(len(string)):
        if string[i] in vowels:
            Kevin += len(string) - i
        else:
            Stuart += len(string) - i
    
    if Stuart > Kevin:
        print('Stuart', Stuart)
    elif Kevin > Stuart:
        print('Kevin', Kevin)
    else:
        print('Draw')


