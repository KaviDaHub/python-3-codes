#multiple inheritance: C(A,B)
#multi level inheritance : CB-> BA -> A
'''class girls:
    def academics(self):
        print("girls are good in academics")
    def sports(self):
        print("girls are best in sports")
class Boys :
    def baseball(self):
        print("Boys are good at baseball")
    def swimming(self):
        print("Boys are good at swimming")
class A(girls,Boys):
    pass
class B(Boys):
    pass
class C(girls):
    pass
class_A=A()
class_B=B()
class_C=C()
class_A.sports()
class_B.swimming()
class_C.baseball()
'''
#multi level inheritance :
class Mine:
    def __init__(self,name):
        self.name=name
        pass
class girls(Mine):
    def academics(self):
        print(f"{self.name} is good in academics")
    def sports(self):
        print(f"{self.name} is best in sports")
class Boys(Mine):
    def baseball(self):
        print(f"{self.name} is good at baseball")
    def swimming(self):
        print(f"{self.name} is good at swimming")
class A(girls):
    pass
class B(Boys):
    pass
class C(Boys):
    pass
class_A=A("kavid")
class_B=B("Ryu Sun Jae ahhh")
class_C=C("kim tae seung")
class_A.sports()
class_B.swimming()
class_C.baseball()
