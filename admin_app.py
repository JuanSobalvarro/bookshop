import tkinter as tk
from tkinter import ttk
import requests
import json

class AdminApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Bookshop Admin")
        self.root.geometry("600x400")
        self.create_widgets()

    def create_widgets(self):
        # Create a frame for the form
        form_frame = ttk.Frame(self.root, padding="10")
        form_frame.grid(row=0, column=0, sticky=(tk.W, tk.E))

        # Book Title
        ttk.Label(form_frame, text="Title:").grid(row=0, column=0, sticky=tk.W)
        self.title_entry = ttk.Entry(form_frame, width=50)
        self.title_entry.grid(row=0, column=1, sticky=(tk.W, tk.E))

        # Author
        ttk.Label(form_frame, text="Author:").grid(row=1, column=0, sticky=tk.W)
        self.author_entry = ttk.Entry(form_frame, width=50)
        self.author_entry.grid(row=1, column=1, sticky=(tk.W, tk.E))

        # Price
        ttk.Label(form_frame, text="Price:").grid(row=2, column=0, sticky=tk.W)
        self.price_entry = ttk.Entry(form_frame, width=50)
        self.price_entry.grid(row=2, column=1, sticky=(tk.W, tk.E))

        # Published Date
        ttk.Label(form_frame, text="Published Date:").grid(row=3, column=0, sticky=tk.W)
        self.published_date_entry = ttk.Entry(form_frame, width=50)
        self.published_date_entry.grid(row=3, column=1, sticky=(tk.W, tk.E))

        # Description
        ttk.Label(form_frame, text="Description:").grid(row=4, column=0, sticky=tk.W)
        self.description_entry = ttk.Entry(form_frame, width=50)
        self.description_entry.grid(row=4, column=1, sticky=(tk.W, tk.E))

        # ISBN
        ttk.Label(form_frame, text="ISBN:").grid(row=5, column=0, sticky=tk.W)
        self.isbn_entry = ttk.Entry(form_frame, width=50)
        self.isbn_entry.grid(row=5, column=1, sticky=(tk.W, tk.E))

        # Create Book Button
        self.create_button = ttk.Button(form_frame, text="Create Book", command=self.create_book)
        self.create_button.grid(row=6, column=1, sticky=(tk.W, tk.E), pady=5)

        # Frame for displaying books
        self.books_frame = ttk.Frame(self.root, padding="10")
        self.books_frame.grid(row=1, column=0, sticky=(tk.W, tk.E))

        self.books_tree = ttk.Treeview(self.books_frame, columns=("title", "author", "price", "published_date", "description", "isbn"), show='headings')
        self.books_tree.heading("title", text="Title")
        self.books_tree.heading("author", text="Author")
        self.books_tree.heading("price", text="Price")
        self.books_tree.heading("published_date", text="Published Date")
        self.books_tree.heading("description", text="Description")
        self.books_tree.heading("isbn", text="ISBN")
        self.books_tree.pack(fill=tk.BOTH, expand=True)

        self.refresh_books()

    def create_book(self):
        book_data = {
            "title": self.title_entry.get(),
            "author": self.author_entry.get(),
            "price": self.price_entry.get(),
            "published_date": self.published_date_entry.get(),
            "description": self.description_entry.get(),
            "isbn": self.isbn_entry.get(),
        }

        response = requests.post("http://127.0.0.1:8000/api/books/", json=book_data)
        if response.status_code == 201:
            self.refresh_books()
        else:
            print(f"Error: {response.status_code}")

    def refresh_books(self):
        response = requests.get("http://127.0.0.1:8000/api/books/")
        if response.status_code == 200:
            books = response.json()
            for row in self.books_tree.get_children():
                self.books_tree.delete(row)
            for book in books:
                self.books_tree.insert("", "end", values=(book["title"], book["author"], book["price"], book["published_date"], book["description"], book["isbn"]))
        else:
            print(f"Error: {response.status_code}")

if __name__ == "__main__":
    root = tk.Tk()
    app = AdminApp(root)
    root.mainloop()
