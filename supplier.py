import tkinter as tk
from tkinter import messagebox
import pickle

class Supplier:
    def __init__(self, supplier_id, name, address, contact_details):
        self.supplier_id = supplier_id
        self.name = name
        self.address = address
        self.contact_details = contact_details

    @staticmethod
    def add():
        add_supplier_window = tk.Toplevel()
        add_supplier_window.title("Add Supplier")
        add_supplier_window.config(bg="#2c3e50")

        # Create a frame to organize entries and labels
        entry_frame = tk.Frame(add_supplier_window, bg="#2c3e50")
        entry_frame.pack(pady=20)

        # Define label width
        label_width = 15

        # Create labels and entry fields
        tk.Label(entry_frame, text="Supplier ID:", bg="#2c3e50", fg="white", width=label_width).grid(row=0, column=0, padx=10, pady=5)
        supplier_id_entry = tk.Entry(entry_frame)
        supplier_id_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(entry_frame, text="Name:", bg="#2c3e50", fg="white", width=label_width).grid(row=1, column=0, padx=10, pady=5)
        name_entry = tk.Entry(entry_frame)
        name_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(entry_frame, text="Address:", bg="#2c3e50", fg="white", width=label_width).grid(row=2, column=0, padx=10, pady=5)
        address_entry = tk.Entry(entry_frame)
        address_entry.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(entry_frame, text="Contact Details:", bg="#2c3e50", fg="white", width=label_width).grid(row=3, column=0, padx=10, pady=5)
        contact_details_entry = tk.Entry(entry_frame)
        contact_details_entry.grid(row=3, column=1, padx=10, pady=5)

        # Save button
        save_button = tk.Button(add_supplier_window, text="Save", command=lambda: save_supplier(
            supplier_id_entry, name_entry, address_entry, contact_details_entry), bg="green", fg="white")
        save_button.pack(pady=10)

    @staticmethod
    def edit():
        edit_supplier_window = tk.Toplevel()
        edit_supplier_window.title("Edit Supplier")
        edit_supplier_window.config(bg="#2c3e50")

        # Create a frame to organize entries and labels
        entry_frame = tk.Frame(edit_supplier_window, bg="#2c3e50")
        entry_frame.pack(pady=20)

        # Define label width
        label_width = 15

        # Create labels and entry fields
        tk.Label(entry_frame, text="Enter Supplier ID to edit:", bg="#2c3e50", fg="white").pack(pady=10)
        supplier_id_entry = tk.Entry(entry_frame)
        supplier_id_entry.pack(pady=5)

        def edit_supplier():
            supplier_id = supplier_id_entry.get()
            with open("binary_supplier.pkl", "rb") as file:
                supplier_data = pickle.load(file)  # Load supplier data as dictionary

            if 'Supplier ID' in supplier_data and supplier_data['Supplier ID'] == supplier_id:
                # Open a new window to edit supplier details
                edit_supplier_window = tk.Toplevel()
                edit_supplier_window.title("Edit Supplier Details")
                edit_supplier_window.config(bg="#2c3e50")

                # Create a frame to organize entries and labels
                entry_frame = tk.Frame(edit_supplier_window, bg="#2c3e50")
                entry_frame.pack(pady=20)

                # Create labels and entry fields
                tk.Label(entry_frame, text="Name:", bg="#2c3e50", fg="white", width=label_width).grid(row=0, column=0, padx=10, pady=5)
                name_entry = tk.Entry(entry_frame)
                name_entry.insert(0, supplier_data['Name'])  # Fill current name
                name_entry.grid(row=0, column=1, padx=10, pady=5)

                tk.Label(entry_frame, text="Address:", bg="#2c3e50", fg="white", width=label_width).grid(row=1, column=0, padx=10, pady=5)
                address_entry = tk.Entry(entry_frame)
                address_entry.insert(0, supplier_data['Address'])  # Fill current address
                address_entry.grid(row=1, column=1, padx=10, pady=5)

                tk.Label(entry_frame, text="Contact Details:", bg="#2c3e50", fg="white", width=label_width).grid(row=2, column=0, padx=10, pady=5)
                contact_details_entry = tk.Entry(entry_frame)
                contact_details_entry.insert(0, supplier_data['Contact Details'])  # Fill current contact details
                contact_details_entry.grid(row=2, column=1, padx=10, pady=5)

                # Save button to update supplier details
                save_button = tk.Button(edit_supplier_window, text="Update", command=lambda: update_supplier(
                    supplier_id, name_entry, address_entry, contact_details_entry), bg="green", fg="white")
                save_button.pack(pady=10)
            else:
                messagebox.showerror("Error", "Supplier ID not found.")

        # Create button to confirm editing
        edit_button = tk.Button(edit_supplier_window, text="Edit", command=edit_supplier, bg="orange", fg="white")
        edit_button.pack(pady=10)

    @staticmethod
    def delete():
        delete_supplier_window = tk.Toplevel()
        delete_supplier_window.title("Delete Supplier")
        delete_supplier_window.config(bg="#2c3e50")

        # Create label and entry for Supplier ID
        tk.Label(delete_supplier_window, text="Enter Supplier ID to delete:", bg="#2c3e50", fg="white").pack(pady=10)
        supplier_id_entry = tk.Entry(delete_supplier_window)
        supplier_id_entry.pack(pady=5)

        def delete_supplier():
            supplier_id = supplier_id_entry.get()
            with open("binary_supplier.pkl", "rb") as file:
                serialized_supplier = file.read()
                supplier_data = pickle.loads(serialized_supplier)

            if 'Supplier ID' in supplier_data and supplier_data['Supplier ID'] == supplier_id:
                del supplier_data['Supplier ID']  # Delete the supplier entry
                with open("binary_supplier.pkl", "wb") as file:
                    pickle.dump(supplier_data, file)  # Write updated data back to file
                messagebox.showinfo("Success", "Supplier deleted successfully.")
            else:
                messagebox.showerror("Error", "Supplier ID not found or does not match.")

        # Create button to confirm deletion
        delete_button = tk.Button(delete_supplier_window, text="Delete", command=delete_supplier, bg="red", fg="white")
        delete_button.pack(pady=10)

    @staticmethod
    def display():
        display_supplier_window = tk.Toplevel()
        display_supplier_window.title("Supplier Details")
        display_supplier_window.config(bg="#2c3e50")

        # Create a frame to organize entries and labels
        entry_frame = tk.Frame(display_supplier_window, bg="#2c3e50")
        entry_frame.pack(pady=20)

        # Define label width
        label_width = 15

        # Create labels and entry fields
        tk.Label(entry_frame, text="Enter Supplier ID:", bg="#2c3e50", fg="white", width=label_width).grid(row=0, column=0, padx=10, pady=5)
        supplier_id_entry = tk.Entry(entry_frame)
        supplier_id_entry.grid(row=0, column=1, padx=10, pady=5)

        def display_supplier():
            supplier_id = supplier_id_entry.get()
            with open("binary_supplier.pkl", "rb") as file:
                supplier_data = pickle.load(file)  # Load supplier data as dictionary

            if 'Supplier ID' in supplier_data and supplier_data['Supplier ID'] == supplier_id:
                display_supplier_details(supplier_data)
            else:
                messagebox.showerror("Error", "Supplier ID not found.")

        # Create button to search and display supplier details
        search_button = tk.Button(entry_frame, text="Search", command=display_supplier, bg="blue", fg="white")
        search_button.grid(row=1, columnspan=2, pady=10)

        def display_supplier_details(supplier_details):
            display_frame = tk.Frame(display_supplier_window, bg="#2c3e50")
            display_frame.pack(pady=20)

            for i, (key, value) in enumerate(supplier_details.items()):
                if key == "Supplier ID":
                    continue
                tk.Label(display_frame, text=key + ":", bg="#2c3e50", fg="white", width=label_width).grid(row=i, column=0, padx=10, pady=5)
                tk.Label(display_frame, text=value, bg="#2c3e50", fg="white").grid(row=i, column=1, padx=10, pady=5)

def save_supplier(supplier_id_entry, name_entry, address_entry, contact_details_entry):
    # Retrieve data from entry fields
    supplier_id = supplier_id_entry.get()
    name = name_entry.get()
    address = address_entry.get()
    contact_details = contact_details_entry.get()

    # Create a dictionary to store supplier data
    supplier_data = {
        "Supplier ID": supplier_id,
        "Name": name,
        "Address": address,
        "Contact Details": contact_details
    }

    # Serialize the dictionary object
    serialized_supplier = pickle.dumps(supplier_data)

    # Write the serialized data to the pickle file
    with open("binary_supplier.pkl", "wb") as file:
        file.write(serialized_supplier)

    messagebox.showinfo("Success", "Supplier added successfully.")

def update_supplier(supplier_id, name_entry, address_entry, contact_details_entry):
    # Retrieve data from entry fields
    name = name_entry.get()
    address = address_entry.get()
    contact_details = contact_details_entry.get()

    # Create a dictionary to store updated supplier data
    updated_supplier_data = {
        "Supplier ID": supplier_id,
        "Name": name,
        "Address": address,
        "Contact Details": contact_details
    }

    # Serialize the updated dictionary object
    serialized_updated_supplier = pickle.dumps(updated_supplier_data)

    # Write the serialized data to the pickle file
    with open("binary_supplier.pkl", "wb") as file:
        file.write(serialized_updated_supplier)

    messagebox.showinfo("Success", "Supplier details updated successfully.")
