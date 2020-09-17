import os
import sys
print('gbg'*5)
pathpy=os.getcwd()#查看当前系统python路径，今天python的path出毛病了，用这个看了下重新设置
#了下path没用，最后还是重新装了遍就好了
print(pathpy)
print(sys.platform)#查看系统平台
for x in 'naizi!':
	print(x)

# from imp import reload as rl #这个是导入一个重置模块
# rl(xxxxxxx)#重置，这两个命令时在IDLE里导入了一个模块（就是文件）时，重载
# 在IDLE中第一次import文件会自动运行，之后就不行了，需要reload才行，此外也可以更
# 改后reload刷新代码，但是！！！！！！！！！IMP模块被弃用了

a='dada'
b='lkaf'
c='fag'
print(a,b,c)

import Py_wr as pw#导入下其他文档
from Py_wr import f,h,k
print(f,h,k)
jl=dir()#dir是查看任何对象内的（模块、数据类型）属性和方法的内置函数，这个呢是显示当先模块的属性
print(jl)
jl=dir(pw)#这个是查看其他模块，前提是必须improt了一个整个模块，from不行from
#是只导入了模块里的某个对象
print(jl)

an=1
exec(open('Pyl_1.py',encoding='utf-8').read())#这是exec模式打开一个模块，他与import不
#同的是他不会真正的导入模块，而是把源码把拷贝过来来执行
print(an)
an=an+an
print(an)
exec(open('Pyl_1.py',encoding='utf-8').read())
print(an)
ss='print(an)'#拷贝ss
exec(ss)#执行ss

import math#介个是高级数学函数模块
print(math.pi)#介个是高级数学模块中的圆周率~

import random#数据模块
print(random.random())#随机数字
player=['D.va','Angela','Widowmaker','Tracer']#随机挑选
print(random.choice(player))

#字符串有不可变性，以下代码来解释字符串在python中的不可变性
s='Angela'
#S[0]='a' #这样会报错哟，就是不支持指定修改
s='a'+s[1:]#这就行
print(s)

sn='adtw'#另一种该单一字符的方式
lsn=list(sn)
lsn[3]='s'
print(lsn)
sn=''.join(lsn)
print(''.join(lsn))
print(sn)

bs=bytearray(b'Angela')
bs.extend(b',Widowmaker,D.va')
print(bs)
bc=bs.decode()
print(bc)