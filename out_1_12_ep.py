class Employees():
    def __int__(self,name,payment,addpayment):
        self.name=name
        self.payment=payment
        self.addpayment=addpayment
    def payadd(self):
        self.payment=int(self.payment)+int(self.addpayment)
    def print_info(self):
        print('The employes '+self.name+' payment is:'+str(self.payment)+\
        ' This year addpayment:'+str(self.addpayment))