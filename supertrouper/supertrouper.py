from supertrouper import blind as stBlind
from supertrouper import blue as stBlue

class SuperTrouper():
    def __init__(self):
        print("Super trouper")

    def getLyrics(self):
        self.blind = stBlind.Blind()
        self.blue = stBlue.Blue()

    def tryAll(self):
        self.blind.getDefinition()

        self.blue.getValue()
        self.blue.setValue("#0066AA")
        print(self.blue.value)

    def __del__(self):
        print ("Bye-bye Abba!")
