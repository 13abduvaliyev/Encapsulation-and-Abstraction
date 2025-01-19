class Developer:
    def __init__(self, surename=None, position  = None, salary=None) -> None:
        self.surename = surename
        self.position = position
        self.salary = salary
        
        
class SoftwareEngineer(Developer):
    def __init__(self, surename=None, position=None, salary=None, bonus = None, department = None) -> None:
        super().__init__(surename, position, salary)
        self.bonus = bonus
        self.department = department
    
    def input_info(self):
        self.surename = input("\nEnter surname: ")
        self.position = input("Enter position: ")
        self.salary = input("Enter  main income: ")
        self.bonus = input("Enter  bonus: ")
        self.department = input("Enter department: ")
        
    def overall(self):
        total_salary = self.salary + self.bonus 
        print(f"Total salary for {self.surename} {self.position}: {total_salary} Department {self.department}")

engineer1 = SoftwareEngineer()
engineer1.input_info()

engineer2 = SoftwareEngineer()
engineer2.input_info()

engineer3 = SoftwareEngineer()
engineer3.input_info()

engineer4 = SoftwareEngineer()
engineer4.input_info()

engineer5 = SoftwareEngineer()
engineer5.input_info()


engineer1.overall()
engineer2.overall()
engineer3.overall()
engineer4.overall()
engineer5.overall()