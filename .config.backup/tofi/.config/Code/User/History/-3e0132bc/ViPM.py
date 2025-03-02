class Vehicle:
    def __init__(self, make, model):
        self.__make = make
        self.__model = model
        self.__state = "stopped"
    
    def move(self):
        print("I am moving!")
        self.__state = "moving"
    
    def stop(self):
        print("I am now stopped.")
        self.__state = "stopped"
    
    def get_make(self):
        return self.__make
    
    def get_model(self):
        return self.__model
    
    def get_state(self):
        return self.__state
    
    def __str__(self):
        return f"{self.get_make()} {self.get_model()} is {self.get_state}"

class Bus(Vehicle):
    def __init__(self, make, model, decks):
        Vehicle.__init__(self, make, model)
        self.__decks_no = decks
    
    def set_decks_no(self, deck):
        self.__decks_no = deck
    
    def get_decks_no(self):
        return self.__decks_no
    
class Car(Vehicle):
    def __init__(self, make, model, doors):
        Vehicle.__init__(self, make, model)
        self.__doors_no = doors
    
    def set_doors_no(self, number):
        self.__doors_no = number
    
    def get_doors_no(self):
        return self.__doors_no
    
    def __str__(self):
        return f"{self.get_make()} {self.get_model()} with {self.get_doors_no()} doors is {self.get_state()}"
    
    