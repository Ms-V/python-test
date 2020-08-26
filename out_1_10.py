class Players():
    def __init__(self,name,age=18):#（注意是每边是两个_）这是定义了个特殊方法,就是当调用类时候都会运行。_这种是为了区分普通方法
        self.name=name#self这个呢，以他为前缀的变量全类都可以使用，是属性
        self.age=age
    def fly(self):
        print(self.name.title()+' is flying now.')
    def fight(self):
        print(self.name.title()+' is fighting now')
playerinfo=Players('angela',30)
print('chose be '+playerinfo.name.title()+'! She is '+str(playerinfo.age)+' old!')
playerinfo.fly()
playerinfo.fight()
playerinfo_1=Players('widowmaker')
print('chose be '+playerinfo_1.name.title()+'! She is '+str(playerinfo_1.age)+' old!')
playerinfo_1.fly()
playerinfo_1.fight()

class User():
    def __init__(self,fname,lname='',rl_times=0):
        self.fname=fname
        self.lname=lname
        self.rt=rl_times
    def d_user(self):
        print('Name:'+self.fname.title()+' '+self.lname.title())
    def g_user(self):
        print('Good day '+self.fname.title()+' '+self.lname.title())
    def adrl(self):
        self.rt+=1
    def rrt(self):
        self.rt=0
    def mrt(self,times):
        if times>=0:
            self.rt=times
        else:
            print('Reset rt error\n')
user_1=User('angela','Dr')
user_1.d_user()
user_1.g_user()
user_2=User('widowmaker',)
user_2.d_user()
user_2.g_user()
user_1.adrl()
print(str(user_1.rt))
user_1.rrt()
print(str(user_1.rt))
user_1.mrt(15)
print(str(user_1.rt))
user_1.mrt(-9)
print(str(user_1.rt))

class Users():
    def __init__(self,name,sex='female',age='18'):
        self.name=name
        self.sex=sex
        self.age=age
        self.wins=0
        self.pos='C'
    def get_info(self):
        allinfo='Name is '+self.name.title()+',Age is '+str(self.age)+',And is '+\
        self.sex.title()+' Total win is:'+str(self.wins)
        return allinfo
    def update_win(self,win):
        if win >= self.wins:
            self.wins=win
        else:
            print('\nSorry!Is a invalid Value.\nUpdate Error in:'+self.name.title()+'\n')
    def update_win_add(self,win):
        if win >= 0:
            self.wins+=win
        else:
            print('\nSorry!Is a invalid Value.\nAdd Error in:'+self.name.title()+'\n')
class Pos():#一个拆分类
    def __init__(self,post='C'):
        self.pos=post
    def p_post(self):
        print('And is a '+self.pos)
    def get_hl(self):
        if self.pos=='C':
            hl='High'
            print('Hign level is '+hl)
        elif self.pos=='T':
            hl='mid'
            print('Hign level is '+hl)
        elif self.pos=='N':
            hl='low'
            print('Hign level is '+hl)
        else:
            print('Hign level is Error')
class Lowuser(Users):#一个子类
    def __init__(self,name,sex='female',age='18'):#这里不继承父类的默认！
        super().__init__(name,sex,age)#super是一种特殊方法，是连接子类和父类的方法
        self.colors='blue'#这是一个子类中的属性，父类不会包含他
        self.post=Pos()
    def p_colors(self):
        print(self.name.title()+' is '+self.colors)
    def update_win_add(self):#在子类中可以重复使用父类的方法命名去取代父类的方法，就是说
        #同名方法子类生效
        print('Sorry can not update win times.Error:low user '+self.name)#Positioning
user_1=Users('angela','female',32)
user_2=Users('Widowmaker')
user_3=Users('ashe','female')
user_4=Users('卤蛋！','male')
user_1.wins=167
user_2.wins=151
user_3.wins=150
print(user_1.get_info())
print(user_2.get_info())
print(user_3.get_info())
print(user_4.get_info())
user_1.update_win(user_1.wins-1)
user_2.update_win_add(3)
user_2.update_win_add(-5)
user_4.update_win(user_4.wins+1)
print(user_1.get_info())
print(user_2.get_info())
print(user_3.get_info())
print(user_4.get_info())
low_user1=Lowuser('Dva','female',20)
low_user2=Lowuser('tracer')
low_user3=Lowuser('brigitte')
low_user2.colors='yellow'
low_user1.update_win(148)
low_user2.update_win(128)
print(low_user1.get_info())
print(low_user2.get_info())
low_user1.p_colors()
low_user2.p_colors()
low_user1.update_win_add()
low_user1.post.pos='T'
print(low_user1.name)
low_user1.post.p_post()
low_user1.post.get_hl()
low_user2.post.pos='C'
print(low_user2.name)
low_user2.post.p_post()
low_user2.post.get_hl()
low_user3.post.pos='NT!'
print(low_user3.name)
low_user3.post.p_post()
low_user3.post.get_hl()

from collections import OrderedDict as od
fl=od()
fl['Dva']='H'
fl['angela']='Q'
fl['widowmaker']='L'
fl['ashe']='K'
fl['Tracer']='Z'
for na,va in fl.items():
    print('Name is :'+na.title()+'\nCode is :'+va)

from random import randint as rd
class Die():
    def __init__(self,side='6',time='3'):
        self.sides=side
        self.times=time
    def roll_die(self):
        while self.times >=0: 
            print('Is:'+str(rd(1,self.sides))+'\n')
            self.times-=1
time_1=Die(6,10)
time_1.roll_die()