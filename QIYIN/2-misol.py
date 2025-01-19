class Taxi:
    def __init__(self, name=None, car=None, price=None, path= None, space= None) -> None:
        self.name = name
        self.car = car
        self.__price = price
        self.__path= path
        self.__space = space
        
    def getter(self):
        self.__price = int(input("\nEnter cost: "))
        
    def setter(self):
        space = int(input("Add space: "))
        if space > 0:
            self.__space = space
            
    def change(self):
        self.name = input("Enter new drivr naem: ")
        self.car = input("Enter car type: ")
        
    
    def show_info(self):
        print(f"\nDriver: {self.name}, Car:{self.car}, Cost:{self.__price}$, Type:{self.__path}, Empty sapce:{self.__space}")



    
taxi1 = Taxi("Eldor", "Tracktor", 1000, "Field", 1)
taxi2 = Taxi("Olim", "Lada", 2000, "Village", 4)

taxis = [taxi1, taxi2]


for Taxi in taxis:
    Taxi.show_info()

for Taxi in taxis:
    Taxi.getter()
    Taxi.setter()
    Taxi.change()


print("Updated information :")
for Taxi in taxis:
    Taxi.show_info()