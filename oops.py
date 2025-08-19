class Employee:
    def __init__(self):
        self.id=123
        self.name="Amit"
        self.designation='SDE'
    def travel(self,desitination):
        print(f"Employee is travel to{desitination}")

sam=Employee()
#print(sam.name)

#sam.travel("kerala")

print(type(sam))
