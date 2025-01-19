class Book:
    def __init__(self, name, page_count, price):
        self.name = name
        self.page_count = page_count
        self.price = price

    def increase_page_count(self):
        self.page_count += 10

    def decrease_price(self):
        if self.page_count > 100:
            self.price /= 2

    def display_info(self):
        print(f"Kitob nomi: {self.name}, Sahifa soni: {self.page_count}, Narxi: {self.price:.2f} som")

books = []
for i in range(5):
    print(f"{i + 1}-kitob uchun ma'lumot kiriting:")
    name = input("Kitob nomini kiriting: ")
    page_count = int(input("Sahifalar sonini kiriting: "))
    price = float(input("Narxini kiriting : "))
    books.append(Book(name, page_count, price))

for book in books:
    book.increase_page_count()
    book.decrease_price()

print("\nResult:")
for book in books:
    book.display_info()
