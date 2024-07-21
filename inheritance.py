#inheritance = allows a class to inherit attributes and methods from another class
# it helps in code reusability and extensibilty
#child parent classn= super class
class VCET:
    def __init__(self,dept):
        self.dept=dept
        print(f"this is the {dept}")
        self.present=True
    def sports(self):
        print(f"the {self.dept} girls got the title of the year in sports")
    def academics(self):
        print(f"the {self.dept} boys got the first rank in academics")
        pass
class dept1(VCET):
    def friends(self):
        print(f"in {self.dept} both girls & boys are friends")
class dept2(VCET):
    pass
class dept3(VCET):
    pass
DEPT1=dept1("ECE")
DEPT2=dept2("CSE")
DEPT3=dept3("IT")
print(DEPT2.present)
DEPT1.sports()
DEPT3.academics()
DEPT1.friends()