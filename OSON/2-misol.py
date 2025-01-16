class Phone:
    def __init__(self, name, number) -> None:
        self._name = name
        self._number = number
    
    def getter(self):
        self._name = input("\nEnter your name: ")
        self._number = input("Enter your phone number : ")
        
    def setter(self):
        print ("\nName: \nPhone number: ")

phones =  []

n = 0  
while n != 3:
    print("\n1.To add info enter ",
          "2..To get info enter ",
          "3.To stop program entr ", sep='\n')
    
    n = int(input("Your choice: "))
    
    phone = Phone()
    if n == 1:
        phone.getter()
        phones.append(phone)
        
    if n == 2:
        for phone in phones:
            phone.setter()