class Car:
    def __init__(self, model, rangi, tezlik, narx, yoqilgi_turi):
        self.model = model
        self.rangi = rangi
        self.__tezlik = tezlik
        self.__narx = narx
        self.__yoqilgi_turi = yoqilgi_turi

    def get_tezlik(self):
        return self.__tezlik

    def set_tezlik(self, yangi_tezlik):
        if yangi_tezlik > 0:
            self.__tezlik = yangi_tezlik
        else:
            print("Tezlik musbat bo'lishi kerak!")

    def set_yoqilgi_turi(self, yangi_yoqilgi_turi):
        self.__yoqilgi_turi = yangi_yoqilgi_turi

    def display_info(self):
        return f"Model: {self.model}, Rang: {self.rangi}, Tezlik: {self.__tezlik} km/soat, Narx: {self.__narx} $, Yoqilg'i turi: {self.__yoqilgi_turi}"

car = Car(model="Malibu premier", rangi="Qora", tezlik=270, narx=35000, yoqilgi_turi="Benzin")

while True:
    print("\nMenyu:")
    print("1. Model va rangi ko'rsatish")
    print("2. Model va rangni o'zgartirish")
    print("3. Tezlikni ko'rsatish")
    print("4. Tezlikni o'zgartirish")
    print("5. Yoqilg'i turini o'zgartirish")
    print("6. Mashina ma'lumotlarini ko'rsatish")
    print("7. Exit")

    tanlov = input("Quyidagi menyulardan birini tanlang: ")

    if tanlov == "1":
        print(f"Model: {car.model}, Rang: {car.rangi}")
    elif tanlov == "2":
        yangi_model = input("Yangi modelni kiriting: ")
        yangi_rang = input("Yangi rangni kiriting: ")
        car.model = yangi_model
        car.rangi = yangi_rang
    elif tanlov == "3":
        print("Tezlik:", car.get_tezlik(), "km/soat")
    elif tanlov == "4":
        yangi_tezlik = int(input("Yangi tezlikni kiriting: "))
        car.set_tezlik(yangi_tezlik)
    elif tanlov == "5":
        yangi_yoqilgi_turi = input("Yangi yoqilg'i turini kiriting: ")
        car.set_yoqilgi_turi(yangi_yoqilgi_turi)
    elif tanlov == "6":
        print(car.display_info())
    elif tanlov == "7":
        print("Exiting...")
        break
    else:
        print("Notogri tanlov, Qayta urinib ko'ring!")
