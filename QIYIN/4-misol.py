class Laptop:
    def __init__(self, brand, price, battery_life) -> None:
        self.brand = brand
        self.price = price
        self.battery_life = battery_life
        
    def apply_discount(self):
        if self.battery_life < 5:
            discount = self.price * 0.1
            self.price -= discount
    
    def check_battery(self):
        self.apply_discount()

    def show_info(self):
        if self.battery_life < 5:
            print(f"Brand: {self.brand}, Price: ${self.price}, Battery Life: {self.battery_life} hours (Battery too low)")
        else:
            print(f"Brand: {self.brand}, Price: ${self.price}, Battery Life: {self.battery_life} hours")


laptop1 = Laptop("Mack", 1500, 5)
laptop2 = Laptop("Samsung", 100, 10)
laptop3 = Laptop("HP", 10000000, 3245346576)
laptop4 = Laptop("Lenova", 10, 1)

laptops = [laptop1, laptop2, laptop3, laptop4]

for laptop in laptops:
    laptop.check_battery()
    laptop.show_info()