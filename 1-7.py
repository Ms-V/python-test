pf=5
pn='lb'
km={'lo':'asp',pn:pf}
print(km)
print(km['lo'])
print(km[pn])#用变量就得，用变量，不能用里面的字符串，不知道为嘛
km[pn]=22
print(km[pn]+11)
km['ls']='no!'
print(km)
lm={}
lm['dt']=['hg','jk']#当然可以加数组啦~
lm['aka']='hn'
bf='jkl'
lm[bf]=8
print(lm)
lm[bf]=19
print(lm)
lm={'x':17,'y':5,'s':'m'}
print('local is: '+str(lm['x'])+'|'+str(lm['y'])+' Speed is :'+lm['s'])
if lm['s']=='h':
    lm['x']=lm['x']+10
    lm['y']=lm['y']+10
elif lm['s']=='m':
    lm['x']=lm['x']+3
    lm['y']=lm['y']+3
elif lm['s']=='l':
    lm['x']=lm['x']+1
    lm['y']=lm['y']+1
else:
    print('is not move')
print('now local is: '+str(lm['x'])+'|'+str(lm['y']))
jk={'lo':'jp','ag':17,'se':'sl','ha':'hahahahaha'}
print(jk)
del jk['ha']
print(jk)
fl={'a':'2b',
    'b':'6k',
    'c':'18t',
    'd':'31g'
    }
print("balabalbalbal "+#一对引号不能换行，必须在同一行
    fl['c'
    ].upper
    (
    )+
    ' !')
for na,va in fl.items():
    print("\n na is:" + na.upper()+'\nva is:'+va)
for name in fl.keys():
    print('na is:'+name)
for name in fl:
    print('na is:'+name)
nac=['a','c','d']
for name in fl:
    if name in nac:
        print('good kill '+name+' '+fl[name])
if nac[2] not in fl:
    print(nac[2]+' not in it')
else:
    print(nac[2]+' in it'+'\tAnd va is '+fl[nac[2]]+' key is:'+
    nac[2])
fal={
    'jall':'apple',
    'kad':'banana',
    'zoa':'orange',
    'nago':'shit!',
    'sals':'computer',
    'angela':'banana'
    #'jall':'orange' 键名是不能重复的重复了会覆盖前面的，但是值无所谓 PS：pyhton居然还通过了
}
for v,a in fal.items():#书上的不按顺序是指，键或值不按照规律输出，而不是不按照所在位置输出
    print(v+' '+a)
print('\n')
for v,a in sorted(fal.items()):#输出键
    print(v+' '+a)
print('\n')
for p in sorted(fal.values()):#输出值
    print(p)
print('\n')
for food in sorted(set(fal.values())):#禁止套娃
    print(food)
print('\n')
aa={'aa':'a1','ab':'a2'}
ac={'ac':'a1','ad':'a2'}
ab={'ab':'a1','ac':'a2'}
al=[aa,ab,ac]
for a in al:
    print(a)
print('\n')

ap=[]
for a in range(1,31,1):#这一段不会重复是因为最终是一个数组不是字典
    new_a={a:a,a+1:a+1}
    ap.append(new_a)
for a in ap:
    print(a)
print('all is '+str(len(ap)))
print('\n')

app=[]
for a in range(0,15,1):
    new_app={'cl':'blue','sd':1,'p':1}
    app.append(new_app)
for i in range(0,15,1):
    if i>4 and i<=9:
        app[i]['cl']='red'
        app[i]['sd']=2
        app[i]['p']=2
    elif i>9:
        app[i]['cl']='black'
        app[i]['sd']=3
        app[i]['p']=2
for a in range(0,len(app),1):
    print(app[a])
print('\n')

rz={'lo':'bj','na':['lq','ymy']}
print(rz)
for a in rz['na']:
    print(a)

pg={
    'angela':['sc','pg','l'],
    'dva':['l','sc'],
    'wm':['sc','pg','l'],
    'bt':['ljm','xg'],
    'lk':['sc','pg','l','ls']
}
for na,tz in pg.items():
    print('\n'+ na.title() + "'s like is:")
    for lg in tz:
        print('\t'+lg)

for na,tz in pg.items():
    print('\n'+ na.title() + "'s like is:"+str(tz))

us={
    'angela':{
        'a':'p',
        'b':'z',
        'c':'c',
    },
    'wm':{
        'a':'t',
        'b':'j',
        'c':'x',
    },
}

for un,uf in us.items():
    print("na:"+un)
    print('wf:'+uf['a']+uf['b']+uf['c'])