mg=input('kiss ') #显示kiss 后输入 input 只接受一个 默认是输入的字符串
print(mg)  #只输出输入的

mh=input() #有显示
print('is '+mh+' time')

po='this is a test of the input and is' #多合一
po +='coooooooool right?' #多合一
mk=input(po)
print('hahahahaha hell '+mk)

ag=input("age is:")
ag=int(ag) #这么整形成int
print('coooollll '+str(ag))
print(ag+1)

ga=input('how old?')
ga=int(ga)
if ga >=18:
    print('do it!!!!!!!!!!')
else:
    print('emmmmmmmmmmmmmmmm~~~')

nu=input('num? ') #余数测试
nu=int(nu)
if nu % 2 == 0:
    print(str(nu)+' is even')
else:
    print(str(nu)+' is odd')

np=input("car?")
print('find car '+np)

ns=input("how many?")
ns=int(ns)
if ns >8 :
    print('full')
else:
    print('go in')

nu=input('num？')
nu=int(nu)
if nu % 10 ==0:
    print('good test')
else:
    print('bad test')

gh=1
while gh<6:# gh<=5
    print(gh)
    gh+=1

msg=''
while msg !='quit': #条件不满足继续停止，你懂吧
    msg=input("ent:")
    if msg !='quit':
        print('go on')
    else:
        print('bye!!!')

psg='gogogogogo'
ac=True
while ac: #大概条件就是 ac = true ,for也可以用
    msg=input('??????? :')
    if msg =='quit':
        ac=False
        print('bye!~')
    elif msg=='break':
        print('b1')
        break
    else:
        print('ssssss go~~~~')

iss=0
while iss <10:
    iss+=1
    if iss % 2 ==0:
        continue
    print(iss)

sr=['angela','dva','widowmaker','brigitte','tracer','ashe','sombra']
ssr=[]
#sorted(sr)
while sr: #默认都是Ture？
    cd=sr.pop()
    print('sr user:'+cd.title())
    ssr.append(cd)
cnum=1
for ssrs in sorted(ssr):
    print(str(cnum)+'.user is '+ssrs.title())
    cnum+=1

sr=['angela','dva','sombra','widowmaker','brigitte','tracer','ashe','sombra','sombra']
print(sr)
while 'sombra' in sr: #循环之后全删了，这个的意思是一直循环到没有'sombra'
    sr.remove('sombra')
print(sr)

sr={'dva':'female','brigitte':'female','tracer':'female','sombra':'female'}
eon= True
for naa,sea in sr.items():
    print(naa+' is a '+sea)
while eon:
    name=input("Name:")
    sex=input("sex:")
    sr[name]=sex
    re=input('Go on? (yes/no)')
    if re.lower() == 'no' or re.lower() == 'n':
        eon=False
        print('bye')
for na,se in sr.items():
    print(na+' is a '+se)

sr={'dva':'female','brigitte':'female','tracer':'female','sombra':'female'}
eon= True
for naa,sea in sr.items():
    print(naa+' is a '+sea)
while eon:
    name=input("Name:")
    sex=input("sex:")
    sr[name]=sex
    re=input('Go on? (yes/no)')
    if re.lower() == 'no' or re.lower() == 'n':
        print('bye')
        break
for na,se in sr.items():
    print(na+' is a '+se)

so=['nt','cz','yy']
fo=[]
while so:
    nc=so.pop()
    print('zb have '+nc)
    fo.append(nc)
for nccc in fo:
    print(nccc)

fo=['a','jj','c','bb','jj','hg','jj']
print('jj out')
while 'jj' in fo:
    fo.remove('jj')
    for vh in fo:
        print(vh)


lo={}
av=True
while av:
    na=input('name or exit:')
    lc=True
    if na.lower()=='exit' or na.lower()=='e':
        av=False
        continue
    else:
        cn=1
        while lc:
            loi=input(str(cn)+'.local is:')
            ts={cn:loi}
            if cn==1:
                lo[na]=ts
            else:
                lo[na][cn]=loi
            rec=input('Go on enter local(exit finish rename change name):')
            if rec.lower()=='exit' or rec.lower()=='e':
                lc=False
                av=False
                continue
            elif rec.lower()=='rename' or rec.lower()=='r':
                break
            else:
                cn+=1
for un,ul in lo.items():
    for uln,ull in ul.items():
        print(un+' like '+str(uln)+'.'+ull)
