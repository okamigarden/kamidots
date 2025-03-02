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
        self.__state = "Not in use"
        self.__current_stop = 0 
        
    
    def set_decks_no(self, deck):
        self.__decks_no = deck
    
    def move(self):
        stops = ["New Street", "Bullring", "Moor Street", "BCU"]
        
        if self.__state == "stopped" and self.__current_stop < len(stops) - 1:
            print(f"The Bus was at {stops[self.__current_stop]} and is now moving to {stops[self.__current_stop + 1]}")
            self.__current_stop += 1
            self.__state = "moving"
        else:
            print("I am finished for today!")
            self.__state = "stopped"
        
    def stop(self):
        return "I am a non-stop bus!"
    
    
    def get_decks_no(self):
        return self.__decks_no
    
    def get_route(self):
        stops = ["New Street", "Bullring", "Moor Street", "BCU"]
        return f"{stops[0]} - {stops[1]} - {stops[2]} - {stops[3]}"
    
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
    
    
bus1 = Bus("make", "West Midlands", 2)
print(bus1.get_route())
bus1.move() # First stop
bus1.move() # Second stop
bus1.move() # Third Stop
bus1.move() # Fourth Stop
bus1.move() # Went past the final stop

print(bus1.stop())