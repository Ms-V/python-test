# import os
# import sys
# print('gbg'*5)
# pathpy=os.getcwd()#查看当前系统python路径，今天python的path出毛病了，用这个看了下重新设置
# #了下path没用，最后还是重新装了遍就好了
# print(pathpy)
# print(sys.platform)#查看系统平台
# for x in 'naizi!':
# 	print(x)

# # from imp import reload as rl #这个是导入一个重置模块
# # rl(xxxxxxx)#重置，这两个命令时在IDLE里导入了一个模块（就是文件）时，重载
# # 在IDLE中第一次import文件会自动运行，之后就不行了，需要reload才行，此外也可以更
# # 改后reload刷新代码，但是！！！！！！！！！IMP模块被弃用了

# a='dada'
# b='lkaf'
# c='fag'
# print(a,b,c)

# import Py_wr as pw#导入下其他文档
# from Py_wr import f,h,k
# print(f,h,k)
# jl=dir()#dir是查看任何对象内的（模块、数据类型）属性和方法的内置函数，这个呢是显示当先模块的属性
# print(jl)
# jl=dir(pw)#这个是查看其他模块，前提是必须improt了一个整个模块，from不行from
# #是只导入了模块里的某个对象
# print(jl)

# an=1
# exec(open('Pyl_1.py',encoding='utf-8').read())#这是exec模式打开一个模块，他与import不
# #同的是他不会真正的导入模块，而是把源码把拷贝过来来执行
# print(an)
# an=an+an
# print(an)
# exec(open('Pyl_1.py',encoding='utf-8').read())
# print(an)
# ss='print(an)'#拷贝ss
# exec(ss)#执行ss

# import math#介个是高级数学函数模块
# print(math.pi)#介个是高级数学模块中的圆周率~

# import random#数据模块
# print(random.random())#随机数字
# player=['D.va','Angela','Widowmaker','Tracer']#随机挑选
# print(random.choice(player))

# #字符串有不可变性，以下代码来解释字符串在python中的不可变性
# s='Angela'
# #S[0]='a' #这样会报错哟，就是不支持指定修改
# s='a'+s[1:]#这就行
# print(s)

# sn='adtw'#另一种改单一字符的方式
# lsn=list(sn)
# lsn[3]='s'
# print(lsn)
# sn=''.join(lsn)
# print(''.join(lsn))
# print(sn)

# bs=bytearray(b'Angela')#二进制模式
# bs.extend(b',Widowmaker,D.va')
# print(bs)
# bc=bs.decode()
# print(bc)

# s='D.va,Angela,Widomaker,Tracer'
# print(str(s.find('a')))#find是查找
# print(s.replace('D.va','Sombra'))#这个替换不会改变源变量的数据
# print(s)

# s='D.va|Angela|Widowmaker|Tracer'
# sline=s.split('|')#介个是分隔符，就是按照所输入的字符把字符串分割成列表
# print(s)
# for line in sline:
# 	print(line)

# s='D.va,Angela,Widowmaker,Tracer'#符号不是字母
# s1='Angela'
# s2='一个大象'
# s3='一个脑瘫2'#2不是字母
# print(s.isalpha())#就是看是不是由字母组成，有一个不是字母都返回false
# print(s1.isalpha())
# print(s2.isalpha())
# print(s3.isalpha())

# s='D.va,Angela,Widowmaker,Tracer'#符号不是字母或者数字
# s1='Angela'
# s2='一个大象'
# s3='一个脑瘫2'
# s4='32432432'
# print(s.isalnum())#就是看是不是由字母或数字组成，有一个不是字母或数字都返回false
# print(s1.isalnum())
# print(s2.isalnum())
# print(s3.isalnum())
# print(s4.isalnum())

# print('%s good!'%('Angela'))#还能这么玩
# print(str(ord('a')))#ord查看单个字符的ASCII数值

s=['angela','tracer','d.va']
s=s+['widowmaker']
sa=['a','b','c']
sa=sa+(['d','e']*2)
print(str(len(s)))#len这列表里数的是列表元素的个数
print(str(len(sa)))
s.reverse()#不排序反序
print(s)
s.sort()
print(s)
s.sort(reverse=True)#排序后反序
print(s)
print(s.pop(2))#抽走一个扔掉~
print(s)
m=s.pop(1)#抽走一个换到别的地方
print(m)
print(s)
s.insert(2,'tracer')
print(s)
s.extend(['d.va'])#在末尾添加，注意要是往列表添加，别忘了加[]，加'xx...'加到列表里
#会被分开成['x','x'...]
print(s)
