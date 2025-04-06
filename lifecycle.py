class partyAnimal:

    def __init__(self,z):
        self.x = 0
        self.name = z

    def party(self) :
            self.x = self.x + 1
            print (self.name,'party count',self.x)

s = partyAnimal("Sally")
s.party()
j = partyAnimal("Jim")

j.party()
s.party()