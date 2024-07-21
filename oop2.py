class ECE:
    def __init__(self,girls,boys,teachers,year):
        self.girls=girls
        self.boys=boys
        self.teachers=teachers
        self.year=year
    def academics(self):
        print(f"{self.boys} boys scored highest ranks in Academics")
    def sports(self):
        print(f"{self.girls} girls scored high ranks in sports")
