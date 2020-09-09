# import unittest#导入测试单元标准库
# from out_1_12_name import get_name as gname
# class Nametest(unittest.TestCase):#测试处理单元，括号中间必须继承unittest.TestCase
#     #python才能知道你在测试
#     def testname(self):
#         allname=gname('d.va','song')
#         self.assertEqual(allname,'d.va song')#assertEqual一个断言方法,用来合适结果是否与期待的一致
# unittest.main()

import unittest
from out_1_12_name import get_name as gname
class Nametest(unittest.TestCase):
    def testname(self):
        allname=gname('d.va','song')#这个东西是这样的，要是上面提
        #供的数据不符合函数的要求，会报错，不会继续下面的代码
        self.assertEqual(allname,'d.va song')#这要是不一致只会显示报错，也会象是失败！
        #报错时注意报错的第一行会显示一个大写的字母，E为ERROR，F为Failed
        #下一行的ERROR会告诉你哪里报错
        #Tracerback告诉你具体原因
        #之后时测试的数量和时间
        #然后是成功与否，失败了会显示失败了几个
    def testmidname(self):
        allname=gname('d.va','song','hana')
        self.assertEqual(allname,'d.va hana song')
unittest.main()
