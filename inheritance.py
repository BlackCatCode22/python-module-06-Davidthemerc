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

class FootballTeam(FootballFan):

    def __init__(self,nam):
        super().__init__(nam)
        self.points = 0

    def fairweather(self):
        self.x = self.x - 1
        print(self.name,"- A party member stopped watching the game. Good job! New Party Count:",self.x)

    # Honestly this should be -1 point in the NFL
    def doink(self):
        self.points = self.points + 0
        print(self.name,"- The kicker doinks the kick! No!")

    def intercepted(self):
        print(self.name,"threw an INTERCEPTION! Turnover!")
        self.x = self.x - 2
        print(self.name,"- Two party members stopped watching the game! New Party Count:",self.x)

s = PartyAnimal("Sally's Team")
s.party()

j = FootballFan("Jim's Team")
j.party()
j.touchdown()
j.extrapoint()

j.touchdown()
j.twopointconversion()

b = FootballTeam("Caleb's Team")
b.party()
b.party()
b.party()
b.party()
b.party()
b.party()
b.touchdown()
b.doink()
b.fairweather()
b.intercepted()