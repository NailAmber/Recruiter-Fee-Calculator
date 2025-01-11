import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from db_functions import add_client, update_client_formula, delete_client, get_all_clients

def refresh_client_list():
    clients = get_all_clients()
    client_list.delete(0, tk.END)
    for client in clients:
        client_list.insert(tk.END, f"{client[1]} (Formula: {client[2]})")

def add_client_gui():
    name = entry_name.get()
    formula = entry_formula.get()
    if name and formula:
        add_client(name, formula)
        refresh_client_list()
        entry_name.delete(0, tk.END)
        entry_formula.delete(0, tk.END)
        messagebox.showinfo("Success", f"Client '{name}' added successfully.")
    else:
        messagebox.showerror("Error", "Please fill in all fields.")

def update_client_gui():
    try:
        selected_client = client_list.get(client_list.curselection()).split(' (')[0]
        new_formula = entry_formula.get()
        if selected_client and new_formula:
            update_client_formula(selected_client, new_formula)
            refresh_client_list()
            entry_formula.delete(0, tk.END)
            messagebox.showinfo("Success", f"Client '{selected_client}' updated successfully.")
    except tk.TclError:
        messagebox.showerror("Error", "Please select a client to update.")

def delete_client_gui():
    try:
        selected_client = client_list.get(client_list.curselection()).split(' (')[0]
        if selected_client:
            delete_client(selected_client)
            refresh_client_list()
            messagebox.showinfo("Success", f"Client '{selected_client}' deleted successfully.")
    except tk.TclError:
        messagebox.showerror("Error", "Please select a client to delete.")

# Create the main window
root = tk.Tk()
root.title("Recruiter Database Management")

# Create main frame
main_frame = tk.Frame(root)
main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

# Create listbox with scrollbar
listbox_frame = tk.Frame(main_frame)
listbox_frame.pack(fill=tk.BOTH, expand=True)

client_list = tk.Listbox(listbox_frame, width=50, height=10)
client_list.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scrollbar = ttk.Scrollbar(listbox_frame, orient=tk.VERTICAL, command=client_list.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
client_list.config(yscrollcommand=scrollbar.set)

# Input fields
input_frame = tk.Frame(main_frame)
input_frame.pack(fill=tk.X, pady=5)

tk.Label(input_frame, text="Client Name:").pack(anchor="w")
entry_name = tk.Entry(input_frame)
entry_name.pack(fill=tk.X)

tk.Label(input_frame, text="Payment Formula:").pack(anchor="w")
entry_formula = tk.Entry(input_frame)
entry_formula.pack(fill=tk.X)

# Buttons
button_frame = tk.Frame(main_frame)
button_frame.pack(fill=tk.X, pady=5)

tk.Button(button_frame, text="Add Client", command=add_client_gui).pack(side=tk.LEFT, fill=tk.X, expand=True)
tk.Button(button_frame, text="Update Client Formula", command=update_client_gui).pack(side=tk.LEFT, fill=tk.X, expand=True)
tk.Button(button_frame, text="Delete Client", command=delete_client_gui).pack(side=tk.LEFT, fill=tk.X, expand=True)

# Initial list load
refresh_client_list()

# Make the main window resizable
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# Run the application
root.mainloop()
