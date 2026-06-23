import tkinter as tk
from tkinter import messagebox

contacts = {}

# function
def refresh_list():
    listbox.delete(0, tk.END)
    for name in contacts:
        listbox.insert(tk.END, name)


def add_contact():
    name = entry_name.get().strip()
    phone = entry_phone.get().strip()
    email = entry_email.get().strip()

    if name == "":
        messagebox.showerror("Error", "Name is required")
        return

    contacts[name] = {"phone": phone, "email": email}
    refresh_list()
    clear_fields()


def delete_contact():
    selected = listbox.curselection()
    if not selected:
        messagebox.showerror("Error", "Select contact first")
        return

    name = listbox.get(selected)
    del contacts[name]
    refresh_list()
    clear_fields()


def show_contact(event):
    selected = listbox.curselection()
    if not selected:
        return

    name = listbox.get(selected)
    entry_name.delete(0, tk.END)
    entry_phone.delete(0, tk.END)
    entry_email.delete(0, tk.END)

    entry_name.insert(0, name)
    entry_phone.insert(0, contacts[name]["phone"])
    entry_email.insert(0, contacts[name]["email"])


def search_contact():
    query = entry_search.get().lower()
    listbox.delete(0, tk.END)

    for name in contacts:
        if query in name.lower():
            listbox.insert(tk.END, name)


def show_all():
    refresh_list()


def clear_fields():
    entry_name.delete(0, tk.END)
    entry_phone.delete(0, tk.END)
    entry_email.delete(0, tk.END)


root = tk.Tk()
root.title("Contact Book (Responsive)")
root.geometry("700x450")

root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

left_frame = tk.Frame(root, padx=10, pady=10)
left_frame.grid(row=0, column=0, sticky="ns")

tk.Label(left_frame, text="Name").pack(anchor="w")
entry_name = tk.Entry(left_frame, width=25)
entry_name.pack(fill="x")

tk.Label(left_frame, text="Phone").pack(anchor="w")
entry_phone = tk.Entry(left_frame, width=25)
entry_phone.pack(fill="x")

tk.Label(left_frame, text="Email").pack(anchor="w")
entry_email = tk.Entry(left_frame, width=25)
entry_email.pack(fill="x")

tk.Button(left_frame, text="Add Contact", command=add_contact).pack(fill="x", pady=5)
tk.Button(left_frame, text="Delete Contact", command=delete_contact).pack(fill="x")

# right frame
right_frame = tk.Frame(root, padx=10, pady=10)
right_frame.grid(row=0, column=1, sticky="nsew")

# responsive config
right_frame.grid_rowconfigure(1, weight=1)
right_frame.grid_columnconfigure(0, weight=1)

# Search bar
search_frame = tk.Frame(right_frame)
search_frame.grid(row=0, column=0, sticky="ew")

search_frame.grid_columnconfigure(0, weight=1)

entry_search = tk.Entry(search_frame)
entry_search.grid(row=0, column=0, sticky="ew")

tk.Button(search_frame, text="Search", command=search_contact).grid(row=0, column=1)
tk.Button(search_frame, text="Show All", command=show_all).grid(row=0, column=2)

# Listbox + Scrollbar
list_frame = tk.Frame(right_frame)
list_frame.grid(row=1, column=0, sticky="nsew")

list_frame.grid_rowconfigure(0, weight=1)
list_frame.grid_columnconfigure(0, weight=1)

scrollbar = tk.Scrollbar(list_frame)
scrollbar.grid(row=0, column=1, sticky="ns")

listbox = tk.Listbox(list_frame, yscrollcommand=scrollbar.set)
listbox.grid(row=0, column=0, sticky="nsew")

scrollbar.config(command=listbox.yview)

listbox.bind("<<ListboxSelect>>", show_contact)

root.mainloop()
