main_library = []
    
def view_books():
    # Assume books is a list of dictionaries, where each dictionary represents a book
    books = main_library

    if len(books) == 0:
        print("No books available in the library.")
    else:
        print("List of books in the library:")
        for book in books:
            print(f"Title: {book['title']}")
            print(f"Author: {book['author']}")
            print(f"Year: {book['year']}")
            print(f"Status: {book['status']}")
            print("----------------------")




def delete_book():
    # Assume books is a list of dictionaries, where each dictionary represents a book
    books = main_library

    book_id = input("Enter the author of the book to delete: ")

    book_found = False
    for book in books:
        if book["author"] == book_id:
            books.remove(book)
            book_found = True
            break

    if book_found:
        print("Book deleted successfully.")
    else:
        print("Book not found.")

def issue_book():
                        # Assume books is a list of dictionaries, where each dictionary represents a book
    books = main_library

    book_id = input("Enter the Author of the book to issue: ")

    book_found = False
    for book in books:
        if book["author"] == book_id:
            if book["status"] == "available":
                book["status"] = "issued"
                print("Book issued successfully.")
            else:
                print("Book is already issued.")
            book_found = True
            break

    if not book_found:
        print("Book not found.")


def return_book():
    # Assume books is a list of dictionaries, where each dictionary represents a book
    books = main_library

    book_id = input("Enter the Author of the book to return: ")

    book_found = False
    for book in books:
        if book["author"] == book_id:
            if book["status"] == "issued":
                book["status"] = "available"
                print("Book returned successfully.")
            else:
                print("Book is already available.")
            book_found = True
            break

    if not book_found:
        print("Book not found.")


def add_book():
    # Logic to add a book to the library
    
    book_title = input("Enter the book title: ")
    book_author = input("Enter the book author: ")
    book_year = input("Enter the book publication year: ")


    dict_book = {
        "title":book_title,
        "author":book_author,
        "year":book_year,
        "status":"available"
    }

    main_library.append(dict_book)
    print("Book added successfully.")

def display_info():
    print("Books added successfully:{}".format(main_library))
    
    
def main():
    while True:
        print("Library Management System")
        print("1. Add Book")
        print("2. View Books")
        print("3. Delete Book")
        print("4. Issue Book")
        print("5. Return Book")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_book()
            display_info()
        elif choice == '2':
            view_books()
        elif choice == '3':
            delete_book()
        elif choice == '4':
            issue_book()
        elif choice == '5':
            return_book()
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")
            
main()


# In[ ]:


main_library = []
    
def view_books():
    # Assume books is a list of dictionaries, where each dictionary represents a book
    books = main_library

    if len(books) == 0:
        print("No books available in the library.")
    else:
        print("List of books in the library:")
        for book in books:
            print(f"Title: {book['title']}")
            print(f"Author: {book['author']}")
            print(f"Year: {book['year']}")
            print(f"Status: {book['status']}")
            print("----------------------")




def delete_book():
    # Assume books is a list of dictionaries, where each dictionary represents a book
    books = main_library

    book_id = input("Enter the author of the book to delete: ")

    book_found = False
    for book in books:
        if book["author"] == book_id:
            books.remove(book)
            book_found = True
            break

    if book_found:
        print("Book deleted successfully.")
    else:
        print("Book not found.")

def issue_book():
                        # Assume books is a list of dictionaries, where each dictionary represents a book
    books = main_library

    book_id = input("Enter the Author of the book to issue: ")

    book_found = False
    for book in books:
        if book["author"] == book_id:
            if book["status"] == "available":
                book["status"] = "issued"
                print("Book issued successfully.")
            else:
                print("Book is already issued.")
            book_found = True
            break

    if not book_found:
        print("Book not found.")


def return_book():
    # Assume books is a list of dictionaries, where each dictionary represents a book
    books = main_library

    book_id = input("Enter the Author of the book to return: ")

    book_found = False
    for book in books:
        if book["author"] == book_id:
            if book["status"] == "issued":
                book["status"] = "available"
                print("Book returned successfully.")
            else:
                print("Book is already available.")
            book_found = True
            break

    if not book_found:
        print("Book not found.")


def add_book():
    # Logic to add a book to the library
    
    book_title = input("Enter the book title: ")
    book_author = input("Enter the book author: ")
    book_year = input("Enter the book publication year: ")


    dict_book = {
        "title":book_title,
        "author":book_author,
        "year":book_year,
        "status":"available"
    }

    main_library.append(dict_book)
    print("Book added successfully.")

def display_info():
    print("Books added successfully:{}".format(main_library))
    
    
def main():
    while True:
        print("Library Management System")
        print("1. Add Book")
        print("2. View Books")
        print("3. Delete Book")
        print("4. Issue Book")
        print("5. Return Book")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_book()
            display_info()
        elif choice == '2':
            view_books()
        elif choice == '3':
            delete_book()
        elif choice == '4':
            issue_book()
        elif choice == '5':
            return_book()
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")
            
main()





