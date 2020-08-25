class Player():
    def _init_(self,name,age):#这是定义了个特殊方法,就是当调用类时候都会运行。_这种是为了区分普通方法
        self.name=name#self这个呢，以他为前缀的变量全类都可以使用，是属性
        self.age=age
    def fly(self):
        print(self.name.title()+'is flying now.')
    def fight(self):
        print(self.name.title()+'is fighting now')