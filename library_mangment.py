import datetime
import os
from colorama import Fore, Back, Style, init
from prettytable import PrettyTable

init(autoreset=True)

class LMS:
    """
    Library Management System
    Modules: Display, Issue Books, Return Books, Add Books
    """

    def __init__(self, list_of_books, library_name):
        self.list_of_books = list_of_books
        self.library_name = library_name
        self.books_dict = {}
        Id = 101
        with open(self.list_of_books) as bk:
            content = bk.readlines()
        for line in content:
            self.books_dict.update({
                str(Id): {
                    "books_title": line.strip(),
                    "lender_name": "",
                    "issue_date": "",
                    "status": "Available"
                }
            })
            Id += 1

    def display_books(self):
        print(Fore.BLUE + Style.BRIGHT + "\n📚 List Of Books\n")
        table = PrettyTable(["Book ID", "Title", "Status"])
        for key, value in self.books_dict.items():
            table.add_row([key, value["books_title"], value["status"]])
        print(table)

    def issue_books(self):
        books_id = input(Fore.YELLOW + "Enter Book ID: ")
        current_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if books_id in self.books_dict.keys():
            book = self.books_dict[books_id]
            print(Fore.BLUE + f"\nFor book: {book['books_title']}\n")
            if book['status'] != 'Available':
                print(Fore.RED + f"This book has already been issued to {book['lender_name']} on {book['issue_date']}")
            else:
                your_name = input(Fore.GREEN + "Enter your name: ")
                book['lender_name'] = your_name
                book['issue_date'] = current_date
                book['status'] = "Issued"
                print(Fore.GREEN + f"✅ Book issued successfully to {your_name} on {book['issue_date']}")
        else:
            print(Fore.RED + "❌ Book ID not found! Try Again.")

    def add_books(self):
        new_book = input(Fore.YELLOW + "Enter book title to add: ")
        if not new_book.strip():
            print(Fore.RED + "❌ Book title cannot be empty!")
            return
        elif len(new_book) > 25:
            print(Fore.RED + "❌ Book title should be less than 25 characters!")
        else:
            with open(self.list_of_books, "a") as nb:
                nb.write(f"{new_book}\n")
            new_id = str(int(max(self.books_dict.keys())) + 1)
            self.books_dict.update({
                new_id: {
                    "books_title": new_book,
                    "lender_name": "",
                    "issue_date": "",
                    "status": "Available"
                }
            })
            print(Fore.GREEN + f"✅ {new_book} has been added successfully!")

    def return_book(self):
        book_id = input(Fore.YELLOW + "Enter the returning Book ID: ")
        if book_id in self.books_dict.keys():
            book = self.books_dict[book_id]
            if book['status'] == "Available":
                print(Fore.RED + "❌ This book is already available in the system!")
            else:
                book['lender_name'] = ""
                book['issue_date'] = ""
                book['status'] = "Available"
                print(Fore.GREEN + "✅ Returned book updated in the system!")
        else:
            print(Fore.RED + "❌ Wrong Book ID! Try Again.")


def main():
    try:
        myLMS = LMS("sample.txt", "My Library")
        press_key_list = {
            'd': 'Display Books',
            'i': 'Issue A Book',
            'a': 'Add A Book',
            'r': 'Return The Book',
            'q': 'Quit'
        }
        key_press = ""
        while key_press != 'q':
            print(Fore.MAGENTA + Style.BRIGHT + f"\n╔════════════════════════════════╗")
            print(Fore.MAGENTA + Style.BRIGHT + f"   Welcome to {myLMS.library_name}   ")
            print(Fore.MAGENTA + Style.BRIGHT + f"╚════════════════════════════════╝\n")
            for key, value in press_key_list.items():
                print(Fore.CYAN + f"Press {key.upper()} → {value}")
            key_press = input(Fore.YELLOW + "\nPress Key: ").lower()
            if key_press == 'i':
                myLMS.issue_books()
            elif key_press == 'a':
                myLMS.add_books()
            elif key_press == 'd':
                myLMS.display_books()
            elif key_press == 'r':
                myLMS.return_book()
            elif key_press == 'q':
                print(Fore.GREEN + "👋 Exiting Library Management System. Goodbye!")
            else:
                print(Fore.RED + "❌ Invalid key! Try again.")
    except Exception as e:
        print(Fore.RED + f"⚠️ Error: {e}")


if __name__ == "__main__":
    main()