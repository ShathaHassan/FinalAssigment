import tkinter as tk
from tkinter import messagebox
import pickle

class Guest:
    def __init__(self, guest_id, name, address, contact_details):
        self.guest_id = guest_id
        self.name = name
        self.address = address
        self.contact_details = contact_details

    @staticmethod
    def add():
        add_guest_window = tk.Toplevel()
        add_guest_window.title("Add Guest")

        # Set background color
        add_guest_window.config(bg="#2c3e50")

        # Create a frame to organize entries and labels
        entry_frame = tk.Frame(add_guest_window, bg="#2c3e50")
        entry_frame.pack(pady=20)

        # Define label width
        label_width = 15

        # Create labels and entry fields
        tk.Label(entry_frame, text="Guest ID:", bg="#2c3e50", fg="white", width=label_width).grid(row=0, column=0, padx=10, pady=5)
        guest_id_entry = tk.Entry(entry_frame)
        guest_id_entry.grid(row=0, column=1, padx=10, pady=5)

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
        save_button = tk.Button(add_guest_window, text="Save", command=lambda: save_guest(
            guest_id_entry, name_entry, address_entry, contact_details_entry), bg="green", fg="white")
        save_button.pack(pady=10)

    @staticmethod
    def edit():
        edit_guest_window = tk.Toplevel()
        edit_guest_window.title("Edit Guest")
        edit_guest_window.config(bg="#2c3e50")

        # Create a frame to organize entries and labels
        entry_frame = tk.Frame(edit_guest_window, bg="#2c3e50")
        entry_frame.pack(pady=20)

        # Define label width
        label_width = 15

        # Create labels and entry fields
        tk.Label(entry_frame, text="Enter Guest ID to edit:", bg="#2c3e50", fg="white").pack(pady=10)
        guest_id_entry = tk.Entry(entry_frame)
        guest_id_entry.pack(pady=5)

        def edit_guest():
            guest_id = guest_id_entry.get()
            with open("binary_guest.pkl", "rb") as file:
                guest_data = pickle.load(file)  # Load guest data as dictionary

            if 'Guest ID' in guest_data and guest_data['Guest ID'] == guest_id:
                # Open a new window to edit guest details
                edit_guest_window = tk.Toplevel()
                edit_guest_window.title("Edit Guest Details")
                edit_guest_window.config(bg="#2c3e50")

                # Create a frame to organize entries and labels
                entry_frame = tk.Frame(edit_guest_window, bg="#2c3e50")
                entry_frame.pack(pady=20)

                # Create labels and entry fields
                tk.Label(entry_frame, text="Name:", bg="#2c3e50", fg="white", width=label_width).grid(row=0, column=0, padx=10, pady=5)
                name_entry = tk.Entry(entry_frame)
                name_entry.insert(0, guest_data['Name'])  # Fill current name
                name_entry.grid(row=0, column=1, padx=10, pady=5)

                tk.Label(entry_frame, text="Address:", bg="#2c3e50", fg="white", width=label_width).grid(row=1, column=0, padx=10, pady=5)
                address_entry = tk.Entry(entry_frame)
                address_entry.insert(0, guest_data['Address'])  # Fill current address
                address_entry.grid(row=1, column=1, padx=10, pady=5)

                tk.Label(entry_frame, text="Contact Details:", bg="#2c3e50", fg="white", width=label_width).grid(row=2, column=0, padx=10, pady=5)
                contact_details_entry = tk.Entry(entry_frame)
                contact_details_entry.insert(0, guest_data['Contact Details'])  # Fill current contact details
                contact_details_entry.grid(row=2, column=1, padx=10, pady=5)

                # Save button to update guest details
                save_button = tk.Button(edit_guest_window, text="Update", command=lambda: update_guest(
                    guest_id, name_entry, address_entry, contact_details_entry), bg="green", fg="white")
                save_button.pack(pady=10)
            else:
                messagebox.showerror("Error", "Guest ID not found.")

        # Create button to confirm editing
        edit_button = tk.Button(edit_guest_window, text="Edit", command=edit_guest, bg="orange", fg="white")
        edit_button.pack(pady=10)

    @staticmethod
    def delete():
        delete_guest_window = tk.Toplevel()
        delete_guest_window.title("Delete Guest")
        delete_guest_window.config(bg="#2c3e50")

        # Create label and entry for Guest ID
        tk.Label(delete_guest_window, text="Enter Guest ID to delete:", bg="#2c3e50", fg="white").pack(pady=10)
        guest_id_entry = tk.Entry(delete_guest_window)
        guest_id_entry.pack(pady=5)

        def delete_guest():
            guest_id = guest_id_entry.get()
            with open("binary_guest.pkl", "rb") as file:
                serialized_guest = file.read()
                guest_data = pickle.loads(serialized_guest)

            if 'Guest ID' in guest_data and guest_data['Guest ID'] == guest_id:
                del guest_data['Guest ID']  # Delete the guest entry
                with open("binary_guest.pkl", "wb") as file:
                    pickle.dump(guest_data, file)  # Write updated data back to file
                messagebox.showinfo("Success", "Guest deleted successfully.")
            else:
                messagebox.showerror("Error", "Guest ID not found or does not match.")

        # Create button to confirm deletion
        delete_button = tk.Button(delete_guest_window, text="Delete", command=delete_guest, bg="red", fg="white")
        delete_button.pack(pady=10)

    @staticmethod
    def display():
        display_guest_window = tk.Toplevel()
        display_guest_window.title("Guest Details")
        display_guest_window.config(bg="#2c3e50")

        # Create a frame to organize entries and labels
        entry_frame = tk.Frame(display_guest_window, bg="#2c3e50")
        entry_frame.pack(pady=20)

        # Define label width
        label_width = 15

        # Create labels and entry fields
        tk.Label(entry_frame, text="Enter Guest ID:", bg="#2c3e50", fg="white", width=label_width).grid(row=0, column=0, padx=10, pady=5)
        guest_id_entry = tk.Entry(entry_frame)
        guest_id_entry.grid(row=0, column=1, padx=10, pady=5)

        def display_guest():
            guest_id = guest_id_entry.get()
            with open("binary_guest.pkl", "rb") as file:
                guest_data = pickle.load(file)  # Load guest data as dictionary

            if 'Guest ID' in guest_data and guest_data['Guest ID'] == guest_id:
                display_guest_details(guest_data)
            else:
                messagebox.showerror("Error", "Guest ID not found.")

        # Create button to search and display guest details
        search_button = tk.Button(entry_frame, text="Search", command=display_guest, bg="blue", fg="white")
        search_button.grid(row=1, columnspan=2, pady=10)

        def display_guest_details(guest_details):
            display_frame = tk.Frame(display_guest_window, bg="#2c3e50")
            display_frame.pack(pady=20)

            for i, (key, value) in enumerate(guest_details.items()):
                if key == "Guest ID":
                    continue
                tk.Label(display_frame, text=key + ":", bg="#2c3e50", fg="white", width=label_width).grid(row=i, column=0, padx=10, pady=5)
                tk.Label(display_frame, text=value, bg="#2c3e50", fg="white").grid(row=i, column=1, padx=10, pady=5)

def save_guest(guest_id_entry, name_entry, address_entry, contact_details_entry):
    # Retrieve data from entry fields
    guest_id = guest_id_entry.get()
    name = name_entry.get()
    address = address_entry.get()
    contact_details = contact_details_entry.get()

    # Create a dictionary to store guest data
    guest_data = {
        "Guest ID": guest_id,
        "Name": name,
        "Address": address,
        "Contact Details": contact_details
    }

    # Serialize the dictionary object
    serialized_guest = pickle.dumps(guest_data)

    # Write the serialized data to the pickle file
    with open("binary_guest.pkl", "wb") as file:
        file.write(serialized_guest)

    messagebox.showinfo("Success", "Guest added successfully.")

def update_guest(guest_id, name_entry, address_entry, contact_details_entry):
    # Retrieve data from entry fields
    name = name_entry.get()
    address = address_entry.get()
    contact_details = contact_details_entry.get()

    # Create a dictionary to store updated guest data
    updated_guest_data = {
        "Guest ID": guest_id,
        "Name": name,
        "Address": address,
        "Contact Details": contact_details
    }

    # Serialize the updated dictionary object
    serialized_updated_guest = pickle.dumps(updated_guest_data)

    # Write the serialized data to the pickle file
    with open("binary_guest.pkl", "wb") as file:
        file.write(serialized_updated_guest)

    messagebox.showinfo("Success", "Guest details updated successfully.")

