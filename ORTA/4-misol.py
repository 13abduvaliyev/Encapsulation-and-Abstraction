class Bookstore:
    def __init__(self, name, location, books, services):
        self.name = name
        self.location = location 
        self.books = books  
        self.services = services 
    def scientific_books(self):
        for book in self.books:
            if "ilmiy" in book.lower():
                return True
        return False

if __name__ == "__main__":
    bookstore1 = Bookstore(
        "Kitoblar", 
        "Toshkent", 
        ["Ilmiy Fizika", "Tarix", "Kimyo", "Matematika"], 
        ["Yetkazib berish"]
    )

    bookstore2 = Bookstore(
        "Badiy Kitoblar", 
        "Samarqand", 
        ["Roman", "Bolalar kitoblari"], 
        ["Xizmatlar mavjud emaas"]
    )

    bookstore3 = Bookstore(
        "Adabiy kitoblar", 
        "Samarqand", 
        ["Ilmiy Biologiya" ], 
        ["Yetkazib berish"]
    )

    bookstores = [bookstore1, bookstore2, bookstore3]

    print("Ilmiy kitoblar mavjud bo'lgan do'konlar:")
    for store in bookstores:
        if store.scientific_books():
            print(f"Do'kon nomi: {store.name}, Joylashuvi: {store.location}, Xizmatlar: {', '.join(store.services)}")
