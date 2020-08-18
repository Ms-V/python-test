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

