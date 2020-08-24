def pizza(size,*food):
    print('Size is:'+str(size)+'\nFood is:')
    for f in food:
        print('-'+f)