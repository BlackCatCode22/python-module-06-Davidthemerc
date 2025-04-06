class PartyAnimal:

    def __init__(self,nam):
        self.x = 0
        self.name = nam
        print(self.name,"constructed")

    def party(self) :
        self.x = self.x + 1
        print(self.name,"party count",self.x)

class FootballFan(PartyAnimal):

    def __init__(self,nam):
        super().__init__(nam)
        self.points = 0

    def touchdown(self):
        self.points = self.points + 6
        self.party()
        print(self.name,"TOUCHDOWN! Points:",self.points)

    def extrapoint(self):
        self.points = self.points + 1
        print(self.name,"EXTRA POINT IS GOOD! Points:",self.points)

    def twopointconversion(self):
        self.points = self.points + 2
        print(self.name,"TWO POINT CONVERSION IS GOOD! Points:",self.points)

s = PartyAnimal("Sally")
s.party()

j = FootballFan("Jim")
j.party()
j.touchdown()
j.extrapoint()

j.touchdown()
j.twopointconversion()