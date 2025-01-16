from os import system
class Staff:
    def __init__(self, fullname, age, position):
        self.fullname = fullname
        self.age = age
        self.position = position   
        
    def getter(self):
        self.fullname = input("Enter  full name: ")
        self.age = input("Enter age: ")
        self.position = input("Enter position: ")

    def setter(self):
        print("FullName: ")

staffs = []

while True:
    print("\n1. Yangi lavozim va ishchi qo'shish ","\n2. Ishchilarning ma'lumotini chiqarish ", "\n3. Yangi ishchi ta'minlash ", "\n4. Ishchining lavozimini almashtirish ", "\n5. Exit ")
    choose = int(input("Biror bir menyuni tanlang: "))
    try: 
        choose != 1 or 2 or 3 or 4 or 5
    except ValueError:
        print("Iltimos mavjud bo'lgan menyuni kiriting! ")

    staff = Staff()

    if choose == 1:
        staff.getter()
        staffs.append(staff)

    if choose == 2:
        for staff in staffs:
            staff.setter()

    if choose == 3:
        count = 0
        p = input("Qaysi lavozimni o'zgartirmoqchisiz: ")
        for staff in staffs:
            if staff.position.upper() == p.upper() and staff.position != None:
                staffs.remove(staff)
                staff.getter()
                staffs.append(staff)
                count += 1
                break
        if count == 0:
            print(f"{p} lavozim mavjud emas ")

    if choose == 4:
        count_2 = 0
        p2 = input("Qaysi ishchining lavozimini o'zgartmoqchisiz ")

        for staff in staffs:
            if staff.position.upper() == p2.upper():
                staff.position = input("Yangi lavozim kiriting: ")
                count_2 += 1
            if count_2 == 0:
                print(f"{p2} lavozim topilmadi!")

    if choose == 5:
        print("Exiting...")
        break

            
    
