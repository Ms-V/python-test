def nt():#函数 跟C一个样
    print('nt小锤')
nt()

def xn(get_c):
    print('wow......'+get_c)
xn(input('what?'))

def ds_me():
    nt() #函数调函数
    print('学个屁！')
ds_me()

def fb(bk):
    print('best ass is '+bk)
fb(input("what is the best ass:"))

def ds(at,pn):#这个dog是默认值
    print("\ni have a "+at)
    print('my '+at+' name is '+pn)
ds('dog','微软')
ds('cat','巨硬')
ds(pn='litianyu',at="fox")#关键字给形参上数值，这样可以避免顺序错误引起的问题
ds(pn='绝世大笨蛋',at='dog')

def ds(pn='litianyu',at='dog'):#这个dog是默认值,不能给前面大概，要么就全都给了
    print("\ni have a "+at)
    print('my '+at+' name is '+pn)
ds('巨硬','cat')
ds()

def ms(size='xl',wp='Coooool!'):
    print('Size is '+size)
    print('word is '+wp)
ms()
ms(wp='Nt')

def nc(city,cn='china'):
    print('The '+city+' in '+cn)
nc('beijing')
nc('new york','USA')
nc(cn='jp',city='tk')

def fn(fn,ln):
    fname=fn+' '+ln
    return fname.title()#返回么 都一样
mk=fn('tianyu','wei')
print(mk)

def fn(fn,ln,mn=''):#就是给个可选的，放到最后也不影响啥的
    if mn:#非空为Ture懂了吧~
        fname=fn+' '+mn+' '+ln
    else:
        fname=fn+' '+ln
    return fname.title()
mk=fn('ty','i')
print(mk)
mk=fn('ty','i','niubi')
print(mk)

def bp(fn,ln,ag=''):
    pn={'firstn':fn,'lastn':ln}
    if ag:
        pn['ag']=ag
    return pn
ms=bp('morithi','wr',18)
print(ms)

def na(fn,ln,mn=''):
    if mn:
        fulln=fn+' '+mn+' '+ln
    else:
        fulln=fn+' '+ln
    return fulln
while True:
    print('q exit or enter Name:')

    fm=input("F:")
    if fm=='q':
        break
    mn=input('M:')
    if mn=='q':
        break
    lm=input('L:')
    if lm=='q':
        break
    an=na(fm,lm,mn)
    print(an)

def gu(names):
    for name in names:
        msg="Hi!"+name.title()+'.'
        print(msg)
usernames=['Angela','widowmaker','dva']
gu(usernames)

g_n=['angela','dva','widowmaker','brigitte','tracer','ashe','sombra']
t_n=[]
while g_n:
    m_n=g_n.pop()
    print('Name in T,Now is:'+m_n)
    t_n.append(m_n)
print('All down')
for name in t_n:
    print(name)

g_n=['angela','dva','widowmaker','brigitte','tracer','ashe','sombra']
t_n=[]
def t_g(gname,tname):
    while gname:
        m_n=gname.pop()
        print('Name in T,Now is:'+m_n)
        tname.append(m_n)
def s_d(d_n):
    print('All down')
    for name in d_n:
        print(name)
t_g(g_n[:],t_n)#这个[:]是说不改动原列表，不加的话，原列表会被抽空，就是切片表示法，就是创建了个副本
s_d(t_n)
s_d(g_n)

g_n=['angela','dva','widowmaker','brigitte','tracer','ashe','sombra']
t_n=[]
def best(gname,aname):
    while gname:
        tg=gname.pop()
        print(tg)
        aname.append(tg)
def show(name):
    print('Now you see the best player.')
    for na in name:
        print('Best player is:'+na)
best(g_n[:],t_n)
show(t_n)
print('..........................')
show(g_n)

def pizza(*print_p):
    print(print_p)
pizza('菠萝味','狗屎味','脑瘫味')
pizza('可爱的天使姐姐味')

def pizza(*print_p):
    print('All is this.')
    for p in print_p:
        print('就是这个味儿:'+p)
pizza('菠萝味','狗屎味','脑瘫味')
pizza('可爱的天使姐姐味')

def b_n(fn,ln,**userinfo):
    user={}
    user['fname']=fn
    user['ln']=ln
    for key,va in userinfo.items():
        user[key]=va
    return user
uninfo=b_n('hana','song',job='pilot',Mecha='dva')
print(uninfo)

def cinfo(car,name,**carinfo):
    carinfo_a={}
    carinfo_a['manufacturer']=car
    carinfo_a['name']=name
    for key,va in carinfo.items():
        carinfo_a[key]=va
    return carinfo_a
car=cinfo('subaru','outback',color='red',tow_package=True)
print(car)

import out_1_9#这个是导入整个模块
import out_1_9 as p#这个是导入整个模块，并起别名p
from out_1_9 import *#这个这个是导入整个模块的所有函数,为什么这么做如果模块中有函数的名称与你的项目中使用的名称相
#同，可能导致意想不到的结果：Python可能遇到多个名称相同的函数或变量，进而覆盖函数，而
#不是分别导入所有的函数。
from out_1_9 import pizza#这个是只导入pizza这个函数
from out_1_9 import pizza as pn#这个是导入后起个别名pn
pn(108,'咖喱味','树皮味','交换机味')#这样就可以用别名pn，不用输入一大串
out_1_9.pizza(52,'电视机味')
p.pizza(87,'黑百合味','卤蛋味','猎空味')#这样就可以用别名p，不用输入一大串