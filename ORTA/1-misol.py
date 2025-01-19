class Car:
    def __init__(self, model, color, price, brand, manufacture_year):
        self.model = model  
        self.color = color  
        self.__price = price  
        self.__brand = brand  
        self.__manufacture_year = manufacture_year  

    def get_price(self):
        return self.__price
    def get_manufacture_year(self):
        return self.__manufacture_year

    def set_price(self, new_price):
        if new_price < 0:
            print("Price cannot be negative!")
        else:
            self.__price = new_price

if __name__ == "__main__":
   
    car = Car("Malibu", "White", 35000, "Chevrolet", 2024)

    print(f"Model: {car.model}")
    print(f"Color: {car.color}")

    new_color = input("Enter new color: ")
    car.color = new_color
    print(f"Updated Color: {car.color}")

    print(f"Price: {car.get_price()} $")
    print(f"Manufacture Year: {car.get_manufacture_year()}")

    new_price = int(input("Enter new price: "))
    car.set_price(new_price)

    print(f"Updated Price: {car.get_price()} $")
