class Book:
    def __init__(self, book_id, title, author, publisher, genre, price, total_pages, available_copies):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.publisher = publisher
        self.genre = genre
        self.price = price
        self.total_pages = total_pages
        self.available_copies = available_copies

    def issue_book(self):
        self.available_copies -= 1
        print("Book Issued")

    def return_book(self):
        self.available_copies += 1
        return("Book Returned")
    
    def update_price(self, new_price):
        self.price = new_price
        print("Price Updated")
    
    def check_availability(self):
        print("Available Copies:", self.available_copies)

    def show_details(self):
        print("Book ID:", self.book_id)
        print("Title:", self.title)
        print("Author:", self.author)
        print("Publisher:", self.publisher)
        print("Genre:", self.genre)
        print("Price:", self.price)
        print("Total Pages:", self.total_pages)
        print("Available Copies:", self.available_copies)

book1 = Book(101, "Python", "ABC", "XYZ", "Education", 500, 350, 5)

book1.show_details()
book1.issue_book()
book1.check_availability()
book1.return_book()
book1.update_price(60)
book1.show_details()



