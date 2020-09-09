from out_1_12_name import get_name as gname
while True:
    first=input('\nFirst name:')
    if first=='q':
        break
    mid=input('Mid name:')
    if first=='q':
        break
    last=input('Last name:')
    if last =='q':
        break
    fullname=gname(first,last,mid)
    print(fullname)