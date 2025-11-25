# 📚 Library Management System (LMS)

A simple yet powerful **console-based Library Management System** built with Python.  
This project allows users to **manage books** in a library with features like displaying available books, issuing books, returning books, and adding new books.  

---

## ✨ Features
- **Display Books** – View all books with their ID, title, and status (Available/Issued).
- **Issue Books** – Borrow a book by entering its ID and your name.
- **Return Books** – Return an issued book and update its availability.
- **Add Books** – Add new books to the library with validation.
- **Colorful Console UI** – Enhanced with `colorama` for colored text and `prettytable` for neat tabular display.
- **Error Handling** – Friendly messages for invalid inputs or duplicate actions.
- **Persistent Storage** – Books are stored in a text file (`sample.txt`) for easy updates.

---

## 🖥️ Tech Stack
- **Python 3**
- [Colorama](https://pypi.org/project/colorama/) – for colored console output
- [PrettyTable](https://pypi.org/project/prettytable/) – for tabular book display

---

- Install dependencies:
pip install colorama prettytable

Create a sample.txt file with book titles (one per line).

Run the program:
python lms.py



📖 Usage
When you run the program, you’ll see a menu with options:
╔════════════════════════════════╗
   Welcome to My Library
╚════════════════════════════════╝

Press D → Display Books
Press I → Issue A Book
Press A → Add A Book
Press R → Return The Book
Press Q → Quit

🎯 Example
- Displaying books:
Book ID   Title             Status
101       Harry Potter      Available
102       The Hobbit        Issued
- Issuing a book:
Enter Book ID: 101
Enter your name: Alice
✅ Book issued successfully to Alice on 2025-11-25 19:20:00



📌 Future Improvements
- GUI version using Tkinter or PyQt
- Database integration (SQLite/MySQL) instead of text file
- User authentication system
- Search and filter books

🤝 Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you’d like to change.

📜 License
This project is licensed under the MIT License.

---




