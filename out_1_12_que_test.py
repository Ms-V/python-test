import unittest
from out_1_12_que import Asurvey
class TestAsurver(unittest.TestCase):
    # def test_store_single_response(self):
    #     que='What player you like?'
    #     my_s=Asurvey(que)
    #     my_s.store_respon('D.va')
    #     self.assertIn('D.va',my_s.respon)#断言测试，是否有
    # def test_store_three_response(self):
    #     que='What player you like?'
    #     my_s=Asurvey(que)
    #     res=['D.va','Angela','Widowmaker']
    #     for re in res:
    #         my_s.store_respon(re)
    #     for re in res:#循环测试你懂的
    #         self.assertIn(re,my_s.respon)
    def setUp(self):
        ques='What player you like?'
        self.my_s=Asurvey(ques)
        self.res=['D.va','Angela','Widowmaker','Ashe']
    def test_store_single_response(self):
        self.my_s.store_respon(self.res[0])#因为时测试一个只是取了数组第一个
        self.assertIn(self.res[0],self.my_s.respon)
    def test_store_four_response(self):
        for re in self.res:
            self.my_s.store_respon(re)
        for re in self.res:
            self.assertIn(re,self.my_s.respon)
unittest.main()