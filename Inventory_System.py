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


def update_product():
    name = entry_name.get()
    new_quantity = entry_quantity.get()

    updated_records = []

    try:
        with open(FILE_NAME, "r") as file:
            records = file.readlines()

        found = False

        for record in records:
            data = record.strip().split(",")

            if data[0] == name:
                data[2] = new_quantity
                found = True

            updated_records.append(",".join(data))

        with open(FILE_NAME, "w") as file:
            for item in updated_records:
                file.write(item + "\n")

        if found:
            messagebox.showinfo("Success", "Stock updated successfully")
        else:
            messagebox.showerror("Error", "Product not found")

        display_records()

    except Exception as e:
        messagebox.showerror("Error", str(e))

def delete_product():
    name = entry_name.get()

    updated_records = []

    try:
        with open(FILE_NAME, "r") as file:
            records = file.readlines()

        found = False

        for record in records:
            data = record.strip().split(",")

            if data[0] != name:
                updated_records.append(record)
            else:
                found = True

        with open(FILE_NAME, "w") as file:
            file.writelines(updated_records)

        if found:
            messagebox.showinfo("Success", "Product deleted successfully")
        else:
            messagebox.showerror("Error", "Product not found")

        display_records()

    except Exception as e:
        messagebox.showerror("Error", str(e))