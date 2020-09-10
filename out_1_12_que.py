class Asurvey():
    def __init__(self,question):
        self.ques=question
        self.respon=[]
    def show_question(self):
        print(self.ques)
    def store_respon(self,new_respon):
        self.respon.append(new_respon)
    def show_respon(self):
        print('All is this:')
        for re in self.respon:
            print('- '+re)