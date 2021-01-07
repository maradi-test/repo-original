class Blue:
    hexacode = "#0000FF"
    def __init__ (self):
        print ("But I don\'t feel blue")
        self.value = self.hexacode
    def setValue (self, newValue):
        self.value = newValue
        print ("The value of blue is set to " + self.value)
    def getValue (self):
        print ("The value of blue is " + self.value)
