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