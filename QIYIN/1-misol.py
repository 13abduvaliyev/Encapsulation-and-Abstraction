class Robot:
    def __init__(self, model_num, area, charge, max_work, status) -> None:
        self.model_num = model_num
        self.area = area
        self.charge = charge
        self.max_work = max_work
        self.status = status
        
    def getter(self):
        print("\n")
        if int(self.charge) <= 20:
            print(f"\nModel number: {self.model_num}\nArea: {self.area}\nBattary {self.charge}%, Zaryadlash kerak\nMax ish vaqti: {self.max_work}\nStatus: {self.status}")
        else:
            print(f"\nModel number: {self.model_num}\nArea: {self.area}\nBattary is {self.charge}%, Battery is enough!\nMaximum working time: {self.max_work}\nStatus: {self.status}")
            
            
    def setter(self):
        model_number = input("Telefon nomini kiriting: ")
        for model in robots:
            if model_number == model.model_num:
                new_time =  int(input("Yangi ish vaqtini kiriting: "))
                if new_time <= 12:
                    model.max_work = new_time
                    print(f"Yangi ish vaqti qo'yildi")
                    break
                else:
                    print(f"Max ish vaqti 20 soat")
                    break
                
    
    def status(self):
        if self.status == "Kutmoqda":
            self.charge = 100
    

robot1 = Robot("ChatGpt_robot", "Internet", 50, 24, "Kutmoqda")
robot2 = Robot("Clear_robot", "Home", 24, 10, "Ishlayapdi")
robot3 = Robot("Teacher_robot", "School", 50, 12, "Kutmoqda")

robots = [robot1, robot2, robot3]
choose = 0

while True:
    try:
        choose != 1 or 2 or 3
    except ValueError:
        print("Bunday buyruq mavjud emas!")

    print("\n1. Mavjud telefonlarni ko'rish: ", 
          "2. Ishlash vaqtini o'zgartirish: ",
          "3. Exit", sep="\n")
    choose = int(input("Buyruqni tanlang: "))
    
    if choose == 1:
        for robot in robots:
            robot.getter()
            
    if choose == 2:
        for robot in robots:
            robot.setter()
    
    if choose == 3:
        print("Exiting...")
        break
    
    