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