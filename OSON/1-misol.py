from os import system

class Staff:
    def __init__(self, fullname=None, age=None, position=None):
        self.fullname = fullname
        self.age = age
        self.position = position   
        
    def getter(self):
        self.fullname = input("Enter full name: ")
        self.age = input("Enter age: ")
        self.position = input("Enter position: ")

    def setter(self):
        print(f"FullName: {self.fullname}\nAge: {self.age}\nPosition: {self.position}")

staffs = []

while True:
    print("\n1. Yangi lavozim va ishchi qo'shish",
          "\n2. Ishchilarning ma'lumotini chiqarish",
          "\n3. Yangi ishchi ta'minlash",
          "\n4. Ishchining lavozimini almashtirish",
          "\n5. Exit")

    try:
        choose = int(input("Biror bir menyuni tanlang: "))
    except ValueError:
        print("Iltimos, raqam kiriting!")
        continue

    if choose == 1:
        staff = Staff()
        staff.getter()
        staffs.append(staff)

    elif choose == 2:
        if staffs:
            for staff in staffs:
                staff.setter()
        else:
            print("Ishchilar ro'yxati bo'sh.")

    elif choose == 3:
        count = 0
        p = input("Qaysi lavozimni o'zgartirmoqchisiz: ")
        for staff in staffs:
            if staff.position and staff.position.upper() == p.upper():
                print(f"Lavozim topildi: {staff.fullname}")
                staff.getter()
                count += 1
                break
        if count == 0:
            print(f"{p} lavozim mavjud emas.")

    elif choose == 4:
        count_2 = 0
        p2 = input("Qaysi ishchining lavozimini o'zgartmoqchisiz: ")

        for staff in staffs:
            if staff.fullname and staff.fullname.upper() == p2.upper():
                staff.position = input("Yangi lavozim kiriting: ")
                print(f"Lavozim yangilandi: {staff.fullname} endi {staff.position} lavozimida.")
                count_2 += 1
                break
        if count_2 == 0:
            print(f"{p2} ismli ishchi topilmadi.")

    elif choose == 5:
        print("Exiting...")
        break

    else:
        print("Notogri tanlov, qaytadan urinib ko'ring.")
