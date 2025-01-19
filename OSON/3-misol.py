class Hayvon:
    def __init__(self, turi=None, yoshi=None):
        self.turi = turi
        self.yoshi = yoshi

    def inputt(self):
        self.turi = input("Hayvon turini kiriting: ")
        self.yoshi = input("Hayvon yoshini kiriting: ")

    def output(self):
        print(f"Turi: {self.turi}\nYoshi: {self.yoshi}")

class Yirtqich(Hayvon):
    def __init__(self, turi=None, yoshi=None, ovchilik_mahorati=None):
        super().__init__(turi, yoshi)
        self.ovchilik_mahorati = ovchilik_mahorati

    def inputt(self):
        super().inputt()
        self.ovchilik_mahorati = input("Ovchilik mahoratini kiriting: ")

    def output(self):
        super().output()
        print(f"Ovchilik mahorati: {self.ovchilik_mahorati}")

class Otxor(Hayvon):
    def __init__(self, turi=None, yoshi=None, sevimli_osimlik=None):
        super().__init__(turi, yoshi)
        self.sevimli_osimlik = sevimli_osimlik

    def inputt(self):
        super().inputt()
        self.sevimli_osimlik = input("Sevimli osimligini kiriting: ")

    def output(self):
        super().output()
        print(f"Sevimli osimlik: {self.sevimli_osimlik}")

hayvonlar = []

while True:
    print("\n1. Yirtqich hayvon qoshish",
          "\n2. Otxor hayvon qoshish",
          "\n3. Barcha hayvonlarni korsatish",
          "\n4. Exit")

    try:
        choose = int(input("Biror bir menyuni tanlang: "))
    except ValueError:
        print("Iltimos, togri raqam kiriting!")
        continue

    if choose == 1:
        yirtqich = Yirtqich()
        yirtqich.inputt()
        hayvonlar.append(yirtqich)

    elif choose == 2:
        otxor = Otxor()
        otxor.inputt()
        hayvonlar.append(otxor)

    elif choose == 3:
        if hayvonlar:
            for hayvon in hayvonlar:
                hayvon.output()
                print("-" * 20)
        else:
            print("Hayvonlar royxati bosh.")

    elif choose == 4:
        print("Exiting...")
        break
    else:
        print("Notogri tanlov, qaytadan urinib koring!")
