import tkinter as tk
from tkinter import messagebox
import pickle

class Event:
    def __init__(self, event_id, event_type, theme, date, time, duration, venue_address, client_id, guest_list, catering_company, cleaning_company, decorations_company, entertainment_company, furniture_supply_company, invoice):
        self.event_id = event_id
        self.event_type = event_type
        self.theme = theme
        self.date = date
        self.time = time
        self.duration = duration
        self.venue_address = venue_address
        self.client_id = client_id
        self.guest_list = guest_list
        self.catering_company = catering_company
        self.cleaning_company = cleaning_company
        self.decorations_company = decorations_company
        self.entertainment_company = entertainment_company
        self.furniture_supply_company = furniture_supply_company
        self.invoice = invoice

    @staticmethod
    def add():
        add_event_window = tk.Toplevel()
        add_event_window.title("Add Event")

        # Set background color
        add_event_window.config(bg="#2c3e50")

        # Create a frame to organize entries and labels
        entry_frame = tk.Frame(add_event_window, bg="#2c3e50")
        entry_frame.pack(pady=20)

        # Define label width
        label_width = 15

        # Create labels and entry fields
        tk.Label(entry_frame, text="Event ID:", bg="#2c3e50", fg="white", width=label_width).grid(row=0, column=0, padx=10, pady=5)
        event_id_entry = tk.Entry(entry_frame)
        event_id_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(entry_frame, text="Event Type:", bg="#2c3e50", fg="white", width=label_width).grid(row=1, column=0, padx=10, pady=5)
        event_type_entry = tk.Entry(entry_frame)
        event_type_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(entry_frame, text="Theme:", bg="#2c3e50", fg="white", width=label_width).grid(row=2, column=0, padx=10, pady=5)
        theme_entry = tk.Entry(entry_frame)
        theme_entry.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(entry_frame, text="Date:", bg="#2c3e50", fg="white", width=label_width).grid(row=3, column=0, padx=10, pady=5)
        date_entry = tk.Entry(entry_frame)
        date_entry.grid(row=3, column=1, padx=10, pady=5)

        tk.Label(entry_frame, text="Time:", bg="#2c3e50", fg="white", width=label_width).grid(row=4, column=0, padx=10, pady=5)
        time_entry = tk.Entry(entry_frame)
        time_entry.grid(row=4, column=1, padx=10, pady=5)

        tk.Label(entry_frame, text="Duration:", bg="#2c3e50", fg="white", width=label_width).grid(row=5, column=0, padx=10, pady=5)
        duration_entry = tk.Entry(entry_frame)
        duration_entry.grid(row=5, column=1, padx=10, pady=5)

        tk.Label(entry_frame, text="Venue Address:", bg="#2c3e50", fg="white", width=label_width).grid(row=6, column=0, padx=10, pady=5)
        venue_address_entry = tk.Entry(entry_frame)
        venue_address_entry.grid(row=6, column=1, padx=10, pady=5)

        tk.Label(entry_frame, text="Client ID:", bg="#2c3e50", fg="white", width=label_width).grid(row=7, column=0, padx=10, pady=5)
        client_id_entry = tk.Entry(entry_frame)
        client_id_entry.grid(row=7, column=1, padx=10, pady=5)

        tk.Label(entry_frame, text="Guest List:", bg="#2c3e50", fg="white", width=label_width).grid(row=8, column=0, padx=10, pady=5)
        guest_list_entry = tk.Entry(entry_frame)
        guest_list_entry.grid(row=8, column=1, padx=10, pady=5)

        tk.Label(entry_frame, text="Catering Company:", bg="#2c3e50", fg="white", width=label_width).grid(row=9, column=0, padx=10, pady=5)
        catering_company_entry = tk.Entry(entry_frame)
        catering_company_entry.grid(row=9, column=1, padx=10, pady=5)

        tk.Label(entry_frame, text="Cleaning Company:", bg="#2c3e50", fg="white", width=label_width).grid(row=10, column=0, padx=10, pady=5)
        cleaning_company_entry = tk.Entry(entry_frame)
        cleaning_company_entry.grid(row=10, column=1, padx=10, pady=5)

        tk.Label(entry_frame, text="Decorations Company:", bg="#2c3e50", fg="white", width=label_width).grid(row=11, column=0, padx=10, pady=5)
        decorations_company_entry = tk.Entry(entry_frame)
        decorations_company_entry.grid(row=11, column=1, padx=10, pady=5)

        tk.Label(entry_frame, text="Entertainment Company:", bg="#2c3e50", fg="white", width=label_width).grid(row=12, column=0, padx=10, pady=5)
        entertainment_company_entry = tk.Entry(entry_frame)
        entertainment_company_entry.grid(row=12, column=1, padx=10, pady=5)

        tk.Label(entry_frame, text="Furniture Supply Company:", bg="#2c3e50", fg="white", width=label_width).grid(row=13, column=0, padx=10, pady=5)
        furniture_supply_company_entry = tk.Entry(entry_frame)
        furniture_supply_company_entry.grid(row=13, column=1, padx=10, pady=5)

        tk.Label(entry_frame, text="Invoice:", bg="#2c3e50", fg="white", width=label_width).grid(row=14, column=0, padx=10, pady=5)
        invoice_entry = tk.Entry(entry_frame)
        invoice_entry.grid(row=14, column=1, padx=10, pady=5)

        # Save button
        save_button = tk.Button(add_event_window, text="Save", command=lambda: save_event(
            event_id_entry, event_type_entry, theme_entry, date_entry, time_entry, duration_entry, venue_address_entry, client_id_entry, guest_list_entry, catering_company_entry, cleaning_company_entry, decorations_company_entry, entertainment_company_entry, furniture_supply_company_entry, invoice_entry), bg="green", fg="white")
        save_button.pack(pady=10)

    @staticmethod
    def edit():
        edit_event_window = tk.Toplevel()
        edit_event_window.title("Edit Event")
        edit_event_window.config(bg="#2c3e50")

        # Create a frame to organize entries and labels
        entry_frame = tk.Frame(edit_event_window, bg="#2c3e50")
        entry_frame.pack(pady=20)

        # Define label width
        label_width = 15

        # Create labels and entry fields
        tk.Label(entry_frame, text="Enter Event ID to edit:", bg="#2c3e50", fg="white").pack(pady=10)
        event_id_entry = tk.Entry(entry_frame)
        event_id_entry.pack(pady=5)

        def edit_event():
            ev_id = event_id_entry.get()
            with open("binary_event.pkl", "rb") as file:
                serialized_event = file.read()
                event_data = pickle.loads(serialized_event)

            if 'Event ID' in event_data and event_data['Event ID'] == ev_id:
                # Open a new window to edit event details
                edit_event_window = tk.Toplevel()
                edit_event_window.title("Edit Event Details")
                edit_event_window.config(bg="#2c3e50")

                # Create a frame to organize entries and labels
                entry_frame = tk.Frame(edit_event_window, bg="#2c3e50")
                entry_frame.pack(pady=20)

                # Create labels and entry fields
                tk.Label(entry_frame, text="Event Type:", bg="#2c3e50", fg="white", width=label_width).grid(row=0, column=0, padx=10, pady=5)
                event_type_entry = tk.Entry(entry_frame)
                event_type_entry.insert(0, event_data['Event Type'])  # Fill current event type
                event_type_entry.grid(row=0, column=1, padx=10, pady=5)

                tk.Label(entry_frame, text="Theme:", bg="#2c3e50", fg="white", width=label_width).grid(row=1, column=0, padx=10, pady=5)
                theme_entry = tk.Entry(entry_frame)
                theme_entry.insert(0, event_data['Theme'])  # Fill current theme
                theme_entry.grid(row=1, column=1, padx=10, pady=5)

                tk.Label(entry_frame, text="Date:", bg="#2c3e50", fg="white", width=label_width).grid(row=2, column=0, padx=10, pady=5)
                date_entry = tk.Entry(entry_frame)
                date_entry.insert(0, event_data['Date'])  # Fill current date
                date_entry.grid(row=2, column=1, padx=10, pady=5)

                tk.Label(entry_frame, text="Time:", bg="#2c3e50", fg="white", width=label_width).grid(row=3, column=0, padx=10, pady=5)
                time_entry = tk.Entry(entry_frame)
                time_entry.insert(0, event_data['Time'])  # Fill current time
                time_entry.grid(row=3, column=1, padx=10, pady=5)

                tk.Label(entry_frame, text="Duration:", bg="#2c3e50", fg="white", width=label_width).grid(row=4, column=0, padx=10, pady=5)
                duration_entry = tk.Entry(entry_frame)
                duration_entry.insert(0, event_data['Duration'])  # Fill current duration
                duration_entry.grid(row=4, column=1, padx=10, pady=5)

                tk.Label(entry_frame, text="Venue Address:", bg="#2c3e50", fg="white", width=label_width).grid(row=5, column=0, padx=10, pady=5)
                venue_address_entry = tk.Entry(entry_frame)
                venue_address_entry.insert(0, event_data['Venue Address'])  # Fill current venue address
                venue_address_entry.grid(row=5, column=1, padx=10, pady=5)

                tk.Label(entry_frame, text="Client ID:", bg="#2c3e50", fg="white", width=label_width).grid(row=6, column=0, padx=10, pady=5)
                client_id_entry = tk.Entry(entry_frame)
                client_id_entry.insert(0, event_data['Client ID'])  # Fill current client ID
                client_id_entry.grid(row=6, column=1, padx=10, pady=5)

                tk.Label(entry_frame, text="Guest List:", bg="#2c3e50", fg="white", width=label_width).grid(row=7, column=0, padx=10, pady=5)
                guest_list_entry = tk.Entry(entry_frame)
                guest_list_entry.insert(0, event_data['Guest List'])  # Fill current guest list
                guest_list_entry.grid(row=7, column=1, padx=10, pady=5)

                tk.Label(entry_frame, text="Catering Company:", bg="#2c3e50", fg="white", width=label_width).grid(row=8, column=0, padx=10, pady=5)
                catering_company_entry = tk.Entry(entry_frame)
                catering_company_entry.insert(0, event_data['Catering Company'])  # Fill current catering company
                catering_company_entry.grid(row=8, column=1, padx=10, pady=5)

                tk.Label(entry_frame, text="Cleaning Company:", bg="#2c3e50", fg="white", width=label_width).grid(row=9, column=0, padx=10, pady=5)
                cleaning_company_entry = tk.Entry(entry_frame)
                cleaning_company_entry.insert(0, event_data['Cleaning Company'])  # Fill current cleaning company
                cleaning_company_entry.grid(row=9, column=1, padx=10, pady=5)

                tk.Label(entry_frame, text="Decorations Company:", bg="#2c3e50", fg="white", width=label_width).grid(row=10, column=0, padx=10, pady=5)
                decorations_company_entry = tk.Entry(entry_frame)
                decorations_company_entry.insert(0, event_data['Decorations Company'])  # Fill current decorations company
                decorations_company_entry.grid(row=10, column=1, padx=10, pady=5)

                tk.Label(entry_frame, text="Entertainment Company:", bg="#2c3e50", fg="white", width=label_width).grid(row=11, column=0, padx=10, pady=5)
                entertainment_company_entry = tk.Entry(entry_frame)
                entertainment_company_entry.insert(0, event_data['Entertainment Company'])  # Fill current entertainment company
                entertainment_company_entry.grid(row=11, column=1, padx=10, pady=5)

                tk.Label(entry_frame, text="Furniture Supply Company:", bg="#2c3e50", fg="white", width=label_width).grid(row=12, column=0, padx=10, pady=5)
                furniture_supply_company_entry = tk.Entry(entry_frame)
                furniture_supply_company_entry.insert(0, event_data['Furniture Supply Company'])  # Fill current furniture supply company
                furniture_supply_company_entry.grid(row=12, column=1, padx=10, pady=5)

                tk.Label(entry_frame, text="Invoice:", bg="#2c3e50", fg="white", width=label_width).grid(row=13, column=0, padx=10, pady=5)
                invoice_entry = tk.Entry(entry_frame)
                invoice_entry.insert(0, event_data['Invoice'])  # Fill current invoice
                invoice_entry.grid(row=13, column=1, padx=10, pady=5)

                # Save button to update event details
                save_button = tk.Button(edit_event_window, text="Update", command=lambda: update_event(
                    ev_id, event_type_entry, theme_entry, date_entry, time_entry, duration_entry, venue_address_entry, client_id_entry,
                    guest_list_entry, catering_company_entry, cleaning_company_entry, decorations_company_entry,
                    entertainment_company_entry, furniture_supply_company_entry, invoice_entry), bg="green", fg="white")
                save_button.pack(pady=10)
            else:
                messagebox.showerror("Error", "Event ID not found or does not match.")

        # Create button to confirm editing
        edit_button = tk.Button(edit_event_window, text="Edit", command=edit_event, bg="orange", fg="white")
        edit_button.pack(pady=10)


    @staticmethod
    def delete():
        delete_event_window = tk.Toplevel()
        delete_event_window.title("Delete Event")
        delete_event_window.config(bg="#2c3e50")

        # Create label and entry for Event ID
        tk.Label(delete_event_window, text="Enter Event ID to delete:", bg="#2c3e50", fg="white").pack(pady=10)
        event_id_entry = tk.Entry(delete_event_window)
        event_id_entry.pack(pady=5)

        def delete_event():
            ev_id = event_id_entry.get()
            with open("binary_event.pkl", "rb") as file:
                serialized_event = file.read()
                event_data = pickle.loads(serialized_event)

            if 'Event ID' in event_data and event_data['Event ID'] == ev_id:
                del event_data['Event ID']  # Delete the event entry
                with open("binary_event.pkl", "wb") as file:
                    pickle.dump(event_data, file)  # Write updated data back to file
                messagebox.showinfo("Success", "Event deleted successfully.")
            else:
                messagebox.showerror("Error", "Event ID not found or does not match.")

        # Create button to confirm deletion
        delete_button = tk.Button(delete_event_window, text="Delete", command=delete_event, bg="red", fg="white")
        delete_button.pack(pady=10)

    @staticmethod
    def display():
        display_window = tk.Toplevel()
        display_window.title("Event Details")
        display_window.config(bg="#2c3e50")
        entry_frame = tk.Frame(display_window, bg="#2c3e50")
        entry_frame.pack(pady=20)
        label_width = 15

        event_id_label = tk.Label(entry_frame, text="Enter Event ID:", bg="#2c3e50", fg="white", width=label_width)
        event_id_label.grid(row=0, column=0, padx=10, pady=5)
        event_id_entry = tk.Entry(entry_frame)
        event_id_entry.grid(row=0, column=1, padx=10, pady=5)

        search_button = tk.Button(entry_frame, text="Search", command=lambda: search_event(event_id_entry), bg="blue", fg="white")
        search_button.grid(row=1, columnspan=2, pady=10)

        def search_event(entry):
            # Retrieve data from pickle file
            with open("binary_event.pkl", "rb") as file:
                serialized_event = file.read()
                event_data = pickle.loads(serialized_event)

            ev_id = entry.get()

            if 'Event ID' in event_data and event_data['Event ID'] == ev_id:
                display_event_details(event_data)
            else:
                messagebox.showerror("Error", "Event ID not found.")

        def display_event_details(event_details):
            display_frame = tk.Frame(display_window, bg="#2c3e50")
            display_frame.pack(pady=20)

            for i, (key, value) in enumerate(event_details.items()):
                tk.Label(display_frame, text=key + ":", bg="#2c3e50", fg="white", width=label_width).grid(row=i, column=0, padx=10, pady=5)
                tk.Label(display_frame, text=value, bg="#2c3e50", fg="white").grid(row=i, column=1, padx=10, pady=5)


def save_event(event_id_entry, event_type_entry, theme_entry, date_entry, time_entry, duration_entry, venue_address_entry, client_id_entry, guest_list_entry, catering_company_entry, cleaning_company_entry, decorations_company_entry, entertainment_company_entry, furniture_supply_company_entry, invoice_entry):
    # Retrieve data from entry fields
    event_id = event_id_entry.get()
    event_type = event_type_entry.get()
    theme = theme_entry.get()
    date = date_entry.get()
    time = time_entry.get()
    duration = duration_entry.get()
    venue_address = venue_address_entry.get()
    client_id = client_id_entry.get()
    guest_list = guest_list_entry.get()
    catering_company = catering_company_entry.get()
    cleaning_company = cleaning_company_entry.get()
    decorations_company = decorations_company_entry.get()
    entertainment_company = entertainment_company_entry.get()
    furniture_supply_company = furniture_supply_company_entry.get()
    invoice = invoice_entry.get()

    # Create a dictionary to store event data
    event_data = {
        "Event ID": event_id,
        "Event Type": event_type,
        "Theme": theme,
        "Date": date,
        "Time": time,
        "Duration": duration,
        "Venue Address": venue_address,
        "Client ID": client_id,
        "Guest List": guest_list,
        "Catering Company": catering_company,
        "Cleaning Company": cleaning_company,
        "Decorations Company": decorations_company,
        "Entertainment Company": entertainment_company,
        "Furniture Supply Company": furniture_supply_company,
        "Invoice": invoice
    }

    # Serialize the dictionary object
    serialized_event = pickle.dumps(event_data)

    # Write the serialized data to the pickle file
    with open("binary_event.pkl", "wb") as file:
        file.write(serialized_event)

    messagebox.showinfo("Success", "Event added successfully.")


def update_event(event_id, event_type_entry, theme_entry, date_entry, time_entry, duration_entry, venue_address_entry, client_id_entry, guest_list_entry, catering_company_entry, cleaning_company_entry, decorations_company_entry, entertainment_company_entry, furniture_supply_company_entry, invoice_entry):
    # Retrieve data from entry fields
    event_type = event_type_entry.get()
    theme = theme_entry.get()
    date = date_entry.get()
    time = time_entry.get()
    duration = duration_entry.get()
    venue_address = venue_address_entry.get()
    client_id = client_id_entry.get()
    guest_list = guest_list_entry.get()
    catering_company = catering_company_entry.get()
    cleaning_company = cleaning_company_entry.get()
    decorations_company = decorations_company_entry.get()
    entertainment_company = entertainment_company_entry.get()
    furniture_supply_company = furniture_supply_company_entry.get()
    invoice = invoice_entry.get()

    # Create a dictionary to store updated event data
    updated_event_data = {
        "Event ID": event_id,
        "Event Type": event_type,
        "Theme": theme,
        "Date": date,
        "Time": time,
        "Duration": duration,
        "Venue Address": venue_address,
        "Client ID": client_id,
        "Guest List": guest_list,
        "Catering Company": catering_company,
        "Cleaning Company": cleaning_company,
        "Decorations Company": decorations_company,
        "Entertainment Company": entertainment_company,
        "Furniture Supply Company": furniture_supply_company,
        "Invoice": invoice
    }

    # Serialize the updated dictionary object
    serialized_updated_event = pickle.dumps(updated_event_data)

    # Write the serialized data to the pickle file
    with open("binary_event.pkl", "wb") as file:
        file.write(serialized_updated_event)

    messagebox.showinfo("Success", "Event details updated successfully.")
