books = []

def add_book():
    id = int(input("Book ID: "))
    title = input("Title: ")
    author = input("Author: ")
    books.append({"book_id": id, "title": title, "author": author, "available": True})
    print("Book Added")

def view_books():
    for book in books:
        print(book)

def search_book():
    id = int(input("Book ID: "))
    for book in books:
        if book["book_id"] == id:
            print(book)
            return
    print("Book Not Found")

def issue_book():
    id = int(input("Book ID: "))
    for book in books:
        if book["book_id"] == id:
            if book["available"]:
                book["available"] = False
                print("Book Issued")
            else:
                print("Already Issued")
            return
    print("Book Not Found")

def return_book():
    id = int(input("Book ID: "))
    for book in books:
        if book["book_id"] == id:
            book["available"] = True
            print("Book Returned")
            return
    print("Book Not Found")

def delete_book():
    id = int(input("Book ID: "))
    for book in books:
        if book["book_id"] == id:
            books.remove(book)
            print("Book Deleted")
            return
    print("Book Not Found")

while True:
    print("\n1.Add 2.View 3.Search 4.Issue 5.Return 6.Delete 7.Exit")
    choice = input("Enter Choice: ")

    if choice == "1":
        add_book()
    elif choice == "2":
        view_books()
    elif choice == "3":
        search_book()
    elif choice == "4":
        issue_book()
    elif choice == "5":
        return_book()
    elif choice == "6":
        delete_book()
    elif choice == "7":
        break
    else:
        print("Invalid Choice")