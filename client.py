import tkinter as tk
from tkinter import messagebox
import pickle

class Client:
    def __init__(self, client_id, name, address, contact_details, budget):
        self.client_id = client_id
        self.name = name
        self.address = address
        self.contact_details = contact_details
        self.budget = budget

    @staticmethod
    def add():
        add_client_window = tk.Toplevel()
        add_client_window.title("Add Client")

        # Set background color
        add_client_window.config(bg="#2c3e50")

        # Create a frame to organize entries and labels
        entry_frame = tk.Frame(add_client_window, bg="#2c3e50")
        entry_frame.pack(pady=20)

        # Define label width
        label_width = 15

        # Create labels and entry fields
        tk.Label(entry_frame, text="Client ID:", bg="#2c3e50", fg="white", width=label_width).grid(row=0, column=0, padx=10, pady=5)
        client_id_entry = tk.Entry(entry_frame)
        client_id_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(entry_frame, text="Name:", bg="#2c3e50", fg="white", width=label_width).grid(row=1, column=0, padx=10, pady=5)
        name_entry = tk.Entry(entry_frame)
        name_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(entry_frame, text="Address:", bg="#2c3e50", fg="white", width=label_width).grid(row=2, column=0, padx=10, pady=5)
        address_entry = tk.Entry(entry_frame)
        address_entry.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(entry_frame, text="Contact Details:", bg="#2c3e50", fg="white", width=label_width).grid(row=3, column=0, padx=10, pady=5)
        contact_details_entry = tk.Entry(entry_frame)
        contact_details_entry.grid(row=3, column=1, padx=10, pady=5)

        tk.Label(entry_frame, text="Budget:", bg="#2c3e50", fg="white", width=label_width).grid(row=4, column=0, padx=10, pady=5)
        budget_entry = tk.Entry(entry_frame)
        budget_entry.grid(row=4, column=1, padx=10, pady=5)

        # Save button
        save_button = tk.Button(add_client_window, text="Save", command=lambda: save_client(
            client_id_entry, name_entry, address_entry, contact_details_entry, budget_entry), bg="green", fg="white")
        save_button.pack(pady=10)

    @staticmethod
    def edit():
        # Create a window to take client ID input for editing
        edit_window = tk.Toplevel()
        edit_window.title("Edit Client")
        edit_window.config(bg="#2c3e50")

        # Create label and entry for Client ID
        tk.Label(edit_window, text="Enter Client ID to edit:", bg="#2c3e50", fg="white").pack(pady=10)
        client_id_entry = tk.Entry(edit_window)
        client_id_entry.pack(pady=5)

        # Define function to edit client
        def edit_client():
            client_id = client_id_entry.get()
            with open("binary_client.pkl", "rb") as file:
                serialized_client = file.read()
                client_data = pickle.loads(serialized_client)

            if 'Client ID' in client_data and client_data['Client ID'] == client_id:
                # Open a new window to edit client details
                edit_client_window = tk.Toplevel()
                edit_client_window.title("Edit Client Details")
                edit_client_window.config(bg="#2c3e50")

                # Create a frame to organize entries and labels
                entry_frame = tk.Frame(edit_client_window, bg="#2c3e50")
                entry_frame.pack(pady=20)

                # Define label width
                label_width = 15

                # Create labels and entry fields
                tk.Label(entry_frame, text="Name:", bg="#2c3e50", fg="white", width=label_width).grid(row=0, column=0, padx=10, pady=5)
                name_entry = tk.Entry(entry_frame)
                name_entry.insert(0, client_data['Name'])  # Fill current name
                name_entry.grid(row=0, column=1, padx=10, pady=5)

                tk.Label(entry_frame, text="Address:", bg="#2c3e50", fg="white", width=label_width).grid(row=1, column=0, padx=10, pady=5)
                address_entry = tk.Entry(entry_frame)
                address_entry.insert(0, client_data['Address'])  # Fill current address
                address_entry.grid(row=1, column=1, padx=10, pady=5)

                tk.Label(entry_frame, text="Contact Details:", bg="#2c3e50", fg="white", width=label_width).grid(row=2, column=0, padx=10, pady=5)
                contact_details_entry = tk.Entry(entry_frame)
                contact_details_entry.insert(0, client_data['Contact Details'])  # Fill current contact details
                contact_details_entry.grid(row=2, column=1, padx=10, pady=5)

                tk.Label(entry_frame, text="Budget:", bg="#2c3e50", fg="white", width=label_width).grid(row=3, column=0, padx=10, pady=5)
                budget_entry = tk.Entry(entry_frame)
                budget_entry.insert(0, client_data['Budget'])  # Fill current budget
                budget_entry.grid(row=3, column=1, padx=10, pady=5)

                # Save button to update client details
                save_button = tk.Button(edit_client_window, text="Update", command=lambda: update_client(client_id, name_entry, address_entry, contact_details_entry, budget_entry), bg="green", fg="white")
                save_button.pack(pady=10)
            else:
                messagebox.showerror("Error", "Client ID not found or does not match.")

        # Create button to confirm editing
        edit_button = tk.Button(edit_window, text="Edit", command=edit_client, bg="orange", fg="white")
        edit_button.pack(pady=10)

    @staticmethod
    def delete():
        # Create a window to take client ID input for deletion
        delete_window = tk.Toplevel()
        delete_window.title("Delete Client")
        delete_window.config(bg="#2c3e50")

        # Create label and entry for Client ID
        tk.Label(delete_window, text="Enter Client ID to delete:", bg="#2c3e50", fg="white").pack(pady=10)
        client_id_entry = tk.Entry(delete_window)
        client_id_entry.pack(pady=5)

        # Define function to delete client
        def delete_client():
            client_id = client_id_entry.get()
            with open("binary_client.pkl", "rb") as file:
                serialized_client = file.read()
                client_data = pickle.loads(serialized_client)

            if 'Client ID' in client_data and client_data['Client ID'] == client_id:
                del client_data['Client ID']  # Delete the client entry
                with open("binary_client.pkl", "wb") as file:
                    pickle.dump(client_data, file)  # Write updated data back to file
                messagebox.showinfo("Success", "Client deleted successfully.")
            else:
                messagebox.showerror("Error", "Client ID not found or does not match.")

        # Create button to confirm deletion
        delete_button = tk.Button(delete_window, text="Delete", command=delete_client, bg="red", fg="white")
        delete_button.pack(pady=10)

    @staticmethod
    def display():
        display_window = tk.Toplevel()
        display_window.title("Client Details")
        display_window.config(bg="#2c3e50")
        entry_frame = tk.Frame(display_window, bg="#2c3e50")
        entry_frame.pack(pady=20)
        label_width = 15

        client_id_label = tk.Label(entry_frame, text="Enter Client ID:", bg="#2c3e50", fg="white", width=label_width)
        client_id_label.grid(row=0, column=0, padx=10, pady=5)
        client_id_entry = tk.Entry(entry_frame)
        client_id_entry.grid(row=0, column=1, padx=10, pady=5)

        search_button = tk.Button(entry_frame, text="Search", command=lambda: search_client(client_id_entry), bg="blue", fg="white")
        search_button.grid(row=1, columnspan=2, pady=10)

        def search_client(entry):
            with open("binary_client.pkl", "rb") as file:
                serialized_client = file.read()
                if serialized_client:
                    client_data = pickle.loads(serialized_client)
                    client_id = entry.get()

                    if 'Client ID' in client_data and client_data['Client ID'] == client_id:
                        display_client_details(client_data)
                    else:
                        messagebox.showerror("Error", "Client ID not found.")
                else:
                    messagebox.showerror("Error", "No client data found.")


        def display_client_details(client_details):
            display_frame = tk.Frame(display_window, bg="#2c3e50")
            display_frame.pack(pady=20)

            for i, (key, value) in enumerate(client_details.items()):
                if key == "Client ID":
                    continue
                tk.Label(display_frame, text=key + ":", bg="#2c3e50", fg="white", width=label_width).grid(row=i, column=0, padx=10, pady=5)
                tk.Label(display_frame, text=value, bg="#2c3e50", fg="white").grid(row=i, column=1, padx=10, pady=5)

def save_client(client_id_entry, name_entry, address_entry, contact_details_entry, budget_entry):
    # Retrieve data from entry fields
    client_id = client_id_entry.get()
    name = name_entry.get()
    address = address_entry.get()
    contact_details = contact_details_entry.get()
    budget = budget_entry.get()

    # Create a dictionary to store client data
    client_data = {
        "Client ID": client_id,
        "Name": name,
        "Address": address,
        "Contact Details": contact_details,
        "Budget": budget
    }

    # Serialize the dictionary object
    serialized_client = pickle.dumps(client_data)

    # Write the serialized data to the pickle file
    with open("binary_client.pkl", "wb") as file:
        file.write(serialized_client)

    messagebox.showinfo("Success", "Client added successfully.")

def update_client(client_id, name_entry, address_entry, contact_details_entry, budget_entry):
    # Retrieve data from entry fields
    name = name_entry.get()
    address = address_entry.get()
    contact_details = contact_details_entry.get()
    budget = budget_entry.get()

    # Create a dictionary to store updated client data
    updated_client_data = {
        "Name": name,
        "Client ID": client_id,
        "Address": address,
        "Contact Details": contact_details,
        "Budget": budget
    }

    # Serialize the updated dictionary object
    serialized_updated_client = pickle.dumps(updated_client_data)

    # Write the serialized data to the pickle file
    with open("binary_client.pkl", "wb") as file:
        file.write(serialized_updated_client)

    messagebox.showinfo("Success", "Client details updated successfully.")

