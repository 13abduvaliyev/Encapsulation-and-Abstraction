class EducationCenter:
    def __init__(self, name):
        self.name = name 

    
class ITCenter(EducationCenter):
    def conduct_class(self):
        return "Conducting programming classes"

class LanguageCenter(EducationCenter):
    def conduct_class(self):
        return "Conducting foreign language classes"

if __name__ == "__main__":
    it_center = ITCenter("Najot Talim")
    language_center = LanguageCenter("Til Markazi")

    while True:
        print("\nQaysi markazning darslarini ko'rmoqchisiz?", 
              "\n1. IT Markazi", 
              "\n2. Til Markazi", 
              "\n3. Chiqish")
        chooce = input("Quyidagi menyulardan birini tanlang: : ")

        if chooce == "1":
            print(f"{it_center.name}: {it_center.conduct_class()}")
        elif chooce == "2":
            print(f"{language_center.name}: {language_center.conduct_class()}")
        elif chooce == "3":
            print("Exiting....")
            break
        else:
            print("Notogri tanlov, qaytadan urinib ko'ring")
