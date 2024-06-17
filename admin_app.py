import tkinter as tk
from tkinter import ttk
import requests
from tkinter import messagebox

API_LINK = "http://127.0.0.1:8000/api/books/"


class AdminApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Bookshop Admin")
        self.root.geometry("1280x720")
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

        try:
            response = requests.post(API_LINK, json=book_data)
            response.raise_for_status()  # Raise exception for 4xx/5xx status codes

            if response.status_code == 201:
                self.refresh_books()
                messagebox.showinfo("Success", "Book created successfully!")
                # Clear entry fields after successful creation
                self.clear_entry_fields()
            else:
                messagebox.showerror("Error", f"Failed to create book. Status code: {response.status_code}")

        except requests.exceptions.RequestException as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    def refresh_books(self):
        try:
            response = requests.get(API_LINK)
            response.raise_for_status()  # Raise exception for 4xx/5xx status codes

            if response.status_code == 200:
                books = response.json()
                self.display_books(books)
            else:
                messagebox.showerror("Error", f"Failed to fetch books. Status code: {response.status_code}")

        except requests.exceptions.RequestException as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    def display_books(self, books):
        # Clear existing data in Treeview
        for row in self.books_tree.get_children():
            self.books_tree.delete(row)

        # Insert new data into Treeview
        for book in books:
            self.books_tree.insert("", "end", values=(book["title"], book["author"], book["price"], book["published_date"], book["description"], book["isbn"]))

    def clear_entry_fields(self):
        # Clear entry fields after successful book creation
        self.title_entry.delete(0, tk.END)
        self.author_entry.delete(0, tk.END)
        self.price_entry.delete(0, tk.END)
        self.published_date_entry.delete(0, tk.END)
        self.description_entry.delete(0, tk.END)
        self.isbn_entry.delete(0, tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    app = AdminApp(root)
    root.mainloop()
