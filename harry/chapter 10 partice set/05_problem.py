from random import randint

class Train:
    
    def __init__(self, trainNO):
        self.trainNO = trainNO   
    
    def book(self, from_place, to):
        print(f"Ticket is booked in train no: {self.trainNO} from {from_place} to {to}")
       
    def getstatus(self):
        print(f"Train no: {self.trainNO} is running on time")
    
    def getfare(self, from_place, to):
        print(f"Ticket fare in train no: {self.trainNO} from {from_place} to {to} is {randint(222,5555)}")

t = Train(12399)

t.book("Lahore", "Karachi")   
t.getstatus()
t.getfare("Lahore", "Karachi")