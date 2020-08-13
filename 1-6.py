cas=['yao','yur','liq','bbw']
for va in cas:
    if va == 'yao':
        print(va.upper())
    else:
        print(va.title())

recas='buau'
if recas != 'kk':
    print('no')

user='sa'
user_2='sh'
user_all=['sa','sg','sf']
if user not in user_all:
    print(user+' not in it')
else:
    print(user+' in it')
if user_2 not in user_all:
    print(user_2 +' not in it')
else:
    print(user_2 +' in it')

car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')
age=15
if age >18 :
    print('balabala')
    print('cacacacaca\tcac\naca')
else:
    print('no')
    print('nonono')

bb=146
if bb >=300:
    pb=15
elif bb>=200 and bb<300:
    pb=10
elif bb<200 and bb>=100:
    pb=8
else:
    pb=6
print(str(pb)+'$')

bc=['a','b','c','d']
if 'z' in bc:
    print('Z')
if 'a' in bc:
    print('A')
if 'b' in bc:
    print('B')

ga=['ba','bb','bba','nt']
for vc in ga:
    if vc=='bba':
        print("no nice "+vc+" no nice!")
    else:
         print("nice "+vc+" nice!")

bg=[]
if bg:
    for bs in bg:
        print(bs)
else:
    print('is null')

aab=['aa','ab','ac','ad','ae','af','ag']
ca=['aa','ad','ae','bb','ag','ff']
for va in ca:
    if va in aab:
        print(va+' have')
    else:
        print(va+' is not have')
print('all finsh')