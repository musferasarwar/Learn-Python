from random import randint

class Train:
    
    def __init__(slf, trainNO):
        slf.trainNO = trainNO   
    
    def book(musfera, from_place, to):
        print(f"Ticket is booked in train no: {musfera.trainNO} from {from_place} to {to}")
       
    def getstatus(self):
        print(f"Train no: {self.trainNO} is running on time")
    
    def getfare(self, from_place, to):
        print(f"Ticket fare in train no: {self.trainNO} from {from_place} to {to} is {randint(222,5555)}")

t = Train(12399)

t.book("Lahore", "Karachi")   
t.getstatus()
t.getfare("Lahore", "Karachi")