import tkinter as tk
from tkinter import messagebox
import pickle


class Venue:
    def __init__(self, venue_id, name, address, contact, min_guests, max_guests):
        self.venue_id = venue_id
        self.name = name
        self.address = address
        self.contact = contact
        self.min_guests = min_guests
        self.max_guests = max_guests

    @staticmethod
    def add():
        add_venue_window = tk.Toplevel()
        add_venue_window.title("Add Venue")

        # Set background color
        add_venue_window.config(bg="#2c3e50")

        # Create a frame to organize entries and labels
        entry_frame = tk.Frame(add_venue_window, bg="#2c3e50")
        entry_frame.pack(pady=20)

        # Define label width
        label_width = 15

        # Create labels and entry fields
        tk.Label(entry_frame, text="Venue ID:", bg="#2c3e50", fg="white", width=label_width).grid(row=0, column=0,
                                                                                                  padx=10, pady=5)
        venue_id_entry = tk.Entry(entry_frame)
        venue_id_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(entry_frame, text="Name:", bg="#2c3e50", fg="white", width=label_width).grid(row=1, column=0, padx=10,
                                                                                              pady=5)
        name_entry = tk.Entry(entry_frame)
        name_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(entry_frame, text="Address:", bg="#2c3e50", fg="white", width=label_width).grid(row=2, column=0,
                                                                                                 padx=10, pady=5)
        address_entry = tk.Entry(entry_frame)
        address_entry.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(entry_frame, text="Contact:", bg="#2c3e50", fg="white", width=label_width).grid(row=3, column=0,
                                                                                                 padx=10, pady=5)
        contact_entry = tk.Entry(entry_frame)
        contact_entry.grid(row=3, column=1, padx=10, pady=5)

        tk.Label(entry_frame, text="Min Guests:", bg="#2c3e50", fg="white", width=label_width).grid(row=4, column=0,
                                                                                                    padx=10, pady=5)
        min_guests_entry = tk.Entry(entry_frame)
        min_guests_entry.grid(row=4, column=1, padx=10, pady=5)

        tk.Label(entry_frame, text="Max Guests:", bg="#2c3e50", fg="white", width=label_width).grid(row=5, column=0,
                                                                                                    padx=10, pady=5)
        max_guests_entry = tk.Entry(entry_frame)
        max_guests_entry.grid(row=5, column=1, padx=10, pady=5)

        # Save button
        save_button = tk.Button(add_venue_window, text="Save", command=lambda: save_venue(
            venue_id_entry, name_entry, address_entry, contact_entry, min_guests_entry, max_guests_entry), bg="green",
                                fg="white")
        save_button.pack(pady=10)

    @staticmethod
    def edit():
        edit_venue_window = tk.Toplevel()
        edit_venue_window.title("Edit Venue")
        edit_venue_window.config(bg="#2c3e50")

        tk.Label(edit_venue_window, text="Enter Venue ID to edit:", bg="#2c3e50", fg="white").pack(pady=10)
        venue_id_entry = tk.Entry(edit_venue_window)
        venue_id_entry.pack(pady=5)

        def edit_venue():
            venue_id = venue_id_entry.get()
            with open("binary_venue.pkl", "rb") as file:
                serialized_venue = file.read()
                venue_data = pickle.loads(serialized_venue)

            if 'Venue ID' in venue_data and venue_data['Venue ID'] == venue_id:
                edit_venue_window = tk.Toplevel()
                edit_venue_window.title("Edit Venue Details")
                edit_venue_window.config(bg="#2c3e50")

                entry_frame = tk.Frame(edit_venue_window, bg="#2c3e50")
                entry_frame.pack(pady=20)

                label_width = 15

                tk.Label(entry_frame, text="Name:", bg="#2c3e50", fg="white", width=label_width).grid(row=0, column=0,
                                                                                                      padx=10, pady=5)
                name_entry = tk.Entry(entry_frame)
                name_entry.insert(0, venue_data['Name'])
                name_entry.grid(row=0, column=1, padx=10, pady=5)

                tk.Label(entry_frame, text="Address:", bg="#2c3e50", fg="white", width=label_width).grid(row=1,
                                                                                                         column=0,
                                                                                                         padx=10,
                                                                                                         pady=5)
                address_entry = tk.Entry(entry_frame)
                address_entry.insert(0, venue_data['Address'])
                address_entry.grid(row=1, column=1, padx=10, pady=5)

                tk.Label(entry_frame, text="Contact:", bg="#2c3e50", fg="white", width=label_width).grid(row=2,
                                                                                                         column=0,
                                                                                                         padx=10,
                                                                                                         pady=5)
                contact_entry = tk.Entry(entry_frame)
                contact_entry.insert(0, venue_data['Contact'])
                contact_entry.grid(row=2, column=1, padx=10, pady=5)

                tk.Label(entry_frame, text="Min Guests:", bg="#2c3e50", fg="white", width=label_width).grid(row=3,
                                                                                                            column=0,
                                                                                                            padx=10,
                                                                                                            pady=5)
                min_guests_entry = tk.Entry(entry_frame)
                min_guests_entry.insert(0, venue_data['Min Guests'])
                min_guests_entry.grid(row=3, column=1, padx=10, pady=5)

                tk.Label(entry_frame, text="Max Guests:", bg="#2c3e50", fg="white", width=label_width).grid(row=4,
                                                                                                            column=0,
                                                                                                            padx=10,
                                                                                                            pady=5)
                max_guests_entry = tk.Entry(entry_frame)
                max_guests_entry.insert(0, venue_data['Max Guests'])
                max_guests_entry.grid(row=4, column=1, padx=10, pady=5)

                save_button = tk.Button(edit_venue_window, text="Update", command=lambda: update_venue(
                    venue_id, name_entry, address_entry, contact_entry, min_guests_entry, max_guests_entry), bg="green",
                                        fg="white")
                save_button.pack(pady=10)
            else:
                messagebox.showerror("Error", "Venue ID not found or does not match.")

        edit_button = tk.Button(edit_venue_window, text="Edit", command=edit_venue, bg="orange", fg="white")
        edit_button.pack(pady=10)

    @staticmethod
    def delete():
        delete_window = tk.Toplevel()
        delete_window.title("Delete Venue")
        delete_window.config(bg="#2c3e50")

        tk.Label(delete_window, text="Enter Venue ID to delete:", bg="#2c3e50", fg="white").pack(pady=10)
        venue_id_entry = tk.Entry(delete_window)
        venue_id_entry.pack(pady=5)

        def delete_venue():
            venue_id = venue_id_entry.get()
            with open("binary_venue.pkl", "rb") as file:
                serialized_venue = file.read()
                venue_data = pickle.loads(serialized_venue)

            if 'Venue ID' in venue_data and venue_data['Venue ID'] == venue_id:
                del venue_data['Venue ID']
                with open("binary_venue.pkl", "wb") as file:
                    pickle.dump(venue_data, file)
                messagebox.showinfo("Success", "Venue deleted successfully.")
            else:
                messagebox.showerror("Error", "Venue ID not found or does not match.")

        delete_button = tk.Button(delete_window, text="Delete", command=delete_venue, bg="red", fg="white")
        delete_button.pack(pady=10)

    @staticmethod
    def display():
        display_window = tk.Toplevel()
        display_window.title("Venue Details")
        display_window.config(bg="#2c3e50")
        entry_frame = tk.Frame(display_window, bg="#2c3e50")
        entry_frame.pack(pady=20)
        label_width = 15

        venue_id_label = tk.Label(entry_frame, text="Enter Venue ID:", bg="#2c3e50", fg="white", width=label_width)
        venue_id_label.grid(row=0, column=0, padx=10, pady=5)
        venue_id_entry = tk.Entry(entry_frame)
        venue_id_entry.grid(row=0, column=1, padx=10, pady=5)

        search_button = tk.Button(entry_frame, text="Search", command=lambda: search_venue(venue_id_entry), bg="blue",
                                  fg="white")
        search_button.grid(row=1, columnspan=2, pady=10)

        def search_venue(entry):
            with open("binary_venue.pkl", "rb") as file:
                serialized_venue = file.read()
                if serialized_venue:
                    venue_data = pickle.loads(serialized_venue)
                    venue_id = entry.get()

                    if 'Venue ID' in venue_data and venue_data['Venue ID'] == venue_id:
                        display_venue_details(venue_data)
                    else:
                        messagebox.showerror("Error", "Venue ID not found.")
                else:
                    messagebox.showerror("Error", "No venues found.")

        def display_venue_details(venue_details):
            display_frame = tk.Frame(display_window, bg="#2c3e50")
            display_frame.pack(pady=20)

            for i, (key, value) in enumerate(venue_details.items()):
                if key == "Venue ID":
                    continue
                tk.Label(display_frame, text=key + ":", bg="#2c3e50", fg="white", width=label_width).grid(row=i,
                                                                                                          column=0,
                                                                                                          padx=10,
                                                                                                          pady=5)
                tk.Label(display_frame, text=value, bg="#2c3e50", fg="white").grid(row=i, column=1, padx=10, pady=5)


def save_venue(venue_id_entry, name_entry, address_entry, contact_entry, min_guests_entry, max_guests_entry):
    venue_id = venue_id_entry.get()
    name = name_entry.get()
    address = address_entry.get()
    contact = contact_entry.get()
    min_guests = min_guests_entry.get()
    max_guests = max_guests_entry.get()

    venue_data = {
        "Venue ID": venue_id,
        "Name": name,
        "Address": address,
        "Contact": contact,
        "Min Guests": min_guests,
        "Max Guests": max_guests
    }

    serialized_venue = pickle.dumps(venue_data)

    with open("binary_venue.pkl", "wb") as file:
        file.write(serialized_venue)

    messagebox.showinfo("Success", "Venue added successfully.")


def update_venue(venue_id, name_entry, address_entry, contact_entry, min_guests_entry, max_guests_entry):
    name = name_entry.get()
    address = address_entry.get()
    contact = contact_entry.get()
    min_guests = min_guests_entry.get()
    max_guests = max_guests_entry.get()

    updated_venue_data = {
        "Venue ID": venue_id,
        "Name": name,
        "Address": address,
        "Contact": contact,
        "Min Guests": min_guests,
        "Max Guests": max_guests
    }

    serialized_updated_venue = pickle.dumps(updated_venue_data)

    with open("binary_venue.pkl", "wb") as file:
        file.write(serialized_updated_venue)

    messagebox.showinfo("Success", "Venue details updated successfully.")
