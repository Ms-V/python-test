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

def cout_w(fn):
    try:
        with open(fn,'r',encoding='utf-8') as t3:#应为是中文系统有时候会提示unicode编码错误,所以转下码
            cp=t3.read()
    except FileNotFoundError:
        print(fn+' is not find')
    else:
        words=cp.split()
        numall=len(words)
        print("The file "+fn+' has about '+str(numall)+' long~~~~')
fn=['Alice’s Adventures in Wonderland.txt','bzingga.txt','taks.txt','taks2.txt']
for fname in fn:
    cout_w(fname)

def cout_w(fn):
    try:
        with open(fn,'r',encoding='utf-8') as t3:
            cp=t3.read()
    except FileNotFoundError:
        pass#这样失败了不会反馈
    else:
        words=cp.split()
        numall=len(words)
        print("The file "+fn+' has about '+str(numall)+' long~~~~')
fn=['Alice’s Adventures in Wonderland.txt','bzingga.txt','taks.txt','taks2.txt']
for fname in fn:
    cout_w(fname)

def addnum(n1,n2):
    try:
        nall=int(n1)+int(n2)
    except ValueError:
        print('The '+n1+' or '+n2+' is not number!')
    else:
        nall=int(n1)+int(n2)
        return nall
def inputnum():
    n1=input('Input n1:')
    if n1=='q':
        exit()
    n2=input('Input n2:')
    if n2=='q':
        exit()
    n=addnum(n1,n2)
    print(str(n))
while True:
    inputnum()

def openfile(fn):
    try:
        with open(fn,'r',encoding='utf-8') as fopen:
            pf=fopen.read()
    except FileNotFoundError:
        pass
    else:
        with open(fn,'r',encoding='utf-8') as fopen:
            print('\n'+fn+' line is:')
            for line in fopen:
                print(line.rstrip())
filename=['sp.txt','mp.txt']
for fn in filename:
    openfile(fn)

def cunta(wd):
    with open('Alice’s Adventures in Wonderland.txt','r',encoding='utf-8') as fo:
        f=fo.read()
        ct=f.lower().count(wd)
        print('The world have '+str(ct))
cw=['alice','the']
for wo in cw:
    cunta(wo)
