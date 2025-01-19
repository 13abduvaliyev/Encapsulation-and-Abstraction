class Avtomobil:
    def __init__(self, name=None, brand=None, price=None):
        self.__name = name
        self.__brand = brand
        self.__price = price

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_brand(self, brand):
        self.__brand = brand

    def get_brand(self):
        return self.__brand

    def set_price(self, price):
        if price < 0:
            print("Narx manfiy bo'lishi mumkin emas!")
        else:
            self.__price = price

    def get_price(self):
        return self.__price

    def update_price(self, new_price):
        if new_price < 0:
            print("Narx manfiy bo'lishi mumkin emas!")
        else:
            self.__price = new_price
            print(f"Yangi narx muvaffaqiyatli o'zgartirildi: {self.__price} $")

car = Avtomobil()

while True:
    print("\n1. Avtomobil nomini kiritish",
          "\n2. Avtomobil markasini kiritish",
          "\n3. Avtomobil narxini kiritish",
          "\n4. Avtomobil narxini o'zgartirish",
          "\n5. Avtomobil ma'lumotlarini ko'rish",
          "\n6. Exit")

    try:
        chooce = int(input("Biror bir menyuni tanlang: "))
    except ValueError:
        print("Iltimos, to'g'ri raqam kiriting!")
        continue

    if chooce == 1:
        name = input("Avtomobil nomini kiriting: ")
        car.set_name(name)

    elif chooce == 2:
        brand = input("Avtomobil markasini kiriting: ")
        car.set_brand(brand)

    elif chooce == 3:
        try:
            price = int(input("Avtomobil narxini kiriting: "))
            car.set_price(price)
        except ValueError:
            print("Iltimos, raqam kiriting!")

    elif chooce == 4:
        try:
            new_price = int(input("Yangi narxni kiriting: "))
            car.update_price(new_price)
        except ValueError:
            print("Iltimos, raqam kiriting!")

    elif chooce == 5:
        print(f"Nom: {car.get_name()}")
        print(f"Marka: {car.get_brand()}")
        print(f"Narx: {car.get_price()} $")

    elif chooce == 6:
        print("Exiting...")
        break

    else:
        print("Notog'ri tanlov, qaytadan urinib ko'ring!")
