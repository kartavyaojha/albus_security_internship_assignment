class programmer:
    def __init__(self,name,language,experience):
        self.name = name
        self.language=language
        self.experience=experience
    
    def display(self):
        print("Name:",self.name)
        print("Language:",self.language)
        print("Experience:",self.experience)

employees=[programmer("Jonathan","French","4 yrs"),programmer("Jose","Spanish","3 yrs"),programmer("Jitin","Hindi","7 yrs")]
for i in employees:
    i.display()
    print("\n")
    