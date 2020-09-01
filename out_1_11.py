with open('pt\out_1_11_t.txt') as filet:#这个是相对路径open()对应的是close(),pt是一个文件夹\是路径符号
    #linux中为/，windows为\
    tp=filet.read()#read()就是读取
    print(tp.rstrip())#rstrip是消除字符串末尾的空白

file_path='C:\\Users\\71476506\\Desktop\\python\\out_1_11_t.txt'#这个是绝对的路径，注意要表示
#\得用两回\\
with open(file_path) as filet_1:
    tp=filet_1.read()
    print(tp.rstrip())

file_path='C:\\Users\\71476506\\Desktop\\python\\out_1_11_t.txt'
with open(file_path) as filet:#open只在with中可用
    for line in filet:
        print(line.rstrip())#就是每个行都自带一个换行符家伙是那个print的换行，就很难受，所以加这个

file_path='C:\\Users\\71476506\\Desktop\\python\\out_1_11_t.txt'
with open(file_path) as filet:
    lineall=filet.readlines()#这个是应为open只能在with里所以先用readlines函数存到列表里
    #方便程序接下来使用
for line in lineall:
    print(line.rstrip())

file_path='C:\\Users\\71476506\\Desktop\\python\\out_1_11_t.txt'
with open(file_path) as filet:
    lineall=filet.readlines()
numall=''
for line in lineall:
    numall+=line.rstrip()#循环增加到字符串里
print(numall)
print(len(numall))

file_path='C:\\Users\\71476506\\Desktop\\python\\p1.txt'
with open(file_path) as filet:
    lineall=filet.readlines()
numall=''
for line in lineall:
    numall+=line.rstrip()#循环增加到字符串里
print(numall[:52]+'......')
print(len(numall))
findnum=input('Enter:')
if findnum in numall:
    print('In it !')
else:
    print('Not in it')

with open('taks.txt') as name:
    nameall=name.readlines()
nameallin=''
for line in nameall:
    nameallin+=line.rstrip()+' '
print(nameallin.replace('dva','Dva'))#前是要改的，后是改成的

with open('taks2.txt','w') as name:
    name.write('sombar\n')#就是不加这个\n就都挤在一行了
    name.write('sombar\n')

with open('taks2.txt','a') as name:#a是附加模式，就是说不会清空而是在结尾添加
    name.write('sombar\n')
    name.write('sombar\n')

with open('taks2.txt','a') as name:
    nameadd=' '
    while nameadd:
        nameadd=input('Enter name:')
        name.write(nameadd+'\n')
with open('taks2.txt','r') as name2:#这就很讨厌，a模式不能读，他妈的
    allname=name2.readlines()
for na in allname:
    print(na.strip())

try:#测试,你懂吧
    print(5/0)
except ZeroDivisionError:#如果不出错跳过！
    print("Can't do that")

while True:
    fnum=input('n1:')
    if fnum=='q':
        break
    snum=input('n2:')
    if snum=='q':
        break
    print(str(int(fnum)/int(snum)))

while True:
    fnum=input('n1:')
    if fnum=='q':
        break
    snum=input('n2:')
    if snum=='q':#套娃使劲套
        break
    else:
        try:
            int(fnum)/int(snum)#简直天才！这也可以做判定的，连函数都省了
        except ZeroDivisionError:
            print('N2 can not was 0')
        else:
            print(str(int(fnum)/int(snum)))

fn='task3.txt'
try:
    with open(fn) as t3:
        cp=t3.readline()
except FileNotFoundError:
    print(fn+' is not find')
else:
    with open(fn) as t3:
        cp=t3.readline()
        print(cp)