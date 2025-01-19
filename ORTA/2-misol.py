class Animal:
    def __init__(self, species, weight):
        self.species = species  
        self.weight = weight 

class Dog(Animal):
    def make_sound(self):
        return "vov-vov"

class Cat(Animal):
    def make_sound(self):
        return "miyov-miyov"

if __name__ == "__main__":
    dog = Dog("It", 15)
    cat = Cat("Mushuk", 5)

    while True:
        print("\nQaysi hayvonning ovozini eshitmoqchisiz?", 
              "\n1. It", 
              "\n2. Mushuk", 
              "\n3. Chiqish")
        chooce = input("Quyidagi menyulardan birini tanlang: ")

        if chooce == "1":
            print(f"{dog.species}: {dog.make_sound()}")
        elif chooce == "2":
            print(f"{cat.species}: {cat.make_sound()}")
        elif chooce == "3":
            print("Exiting...")
            break
        else:
            print("Notogri tanlov, qaytadan urinib ko'ring")
