from tkinter import *
from tkinter import messagebox
import os

FILE_NAME = "inventory.txt"


def add_product():
    name = entry_name.get()
    unit = entry_unit.get()
    quantity = entry_quantity.get()
    price = entry_price.get()

    if name == "" or unit == "" or quantity == "" or price == "":
        messagebox.showerror("Error", "All fields are required!")
        return

    try:
        with open(FILE_NAME, "a") as file:
            file.write(f"{name},{unit},{quantity},{price}\n")

        messagebox.showinfo("Success", "Product added successfully!")

        clear_fields()
        display_records()

    except Exception as e:
        messagebox.showerror("Error", str(e))
    
    def display_records():
    listbox.delete(0, END)

    try:
        if os.path.exists(FILE_NAME):
            with open(FILE_NAME, "r") as file:
                records = file.readlines()

                for record in records:
                    listbox.insert(END, record.strip())

    except Exception as e:
        messagebox.showerror("Error", str(e))


def search_product():
    keyword = entry_search.get()

    listbox.delete(0, END)

    try:
        with open(FILE_NAME, "r") as file:
            records = file.readlines()

            found = False

            for record in records:
                if keyword.lower() in record.lower():
                    listbox.insert(END, record.strip())
                    found = True

            if not found:
                messagebox.showinfo("Search", "Product not found")

    except FileNotFoundError:
        messagebox.showerror("Error", "No inventory file found")