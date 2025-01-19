class Telefon:
    def __init__(self, name=None, number=None):
        self.name = name
        self.number = number

    def getter(self):
        self.name = input("\nEnter name: ")
        self.number = input("Enter phone number: +998")

    def setter(self):
        print(f"\nName: {self.name}\nPhone Number: +998{self.number}")

contacts = []

while True:
    print("\n1. Add contact", "\n2. Show contacts", "\n3. Exit")    
    choose = input("Quyidagi menyulardan birini tanlang: ")

    if choose == '1':
        contact = Telefon()
        contact.getter()
        contacts.append(contact)
    elif choose == '2':
        if contacts:
            for contact in contacts:
                contact.setter()
        else:
            print("\nKontaktlar ro'yxati bo'sh.")
    elif choose == '3':
        print("Exiting...")
        break
    else:
        print("\nNotogri tanlov, qayta urinib ko'ring.")