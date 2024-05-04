import tkinter as tk
from PIL import ImageTk, Image
from emplyee import Employee
from client import Client
from event import Event
from guest import Guest
from venue import Venue
from supplier import Supplier



def main():
    root = tk.Tk()
    root.title("Event Management System")
    root.geometry("600x500")

    # Adding a background image
    background_image = Image.open("background_image.jpg")
    background_image = background_image.resize((600, 500), Image.LANCZOS)
    background_image = ImageTk.PhotoImage(background_image)
    background_label = tk.Label(root, image=background_image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    title_label = tk.Label(root, text="Event Management System", font=("Helvetica", 20, "bold"))
    title_label.place(relx=0.5, rely=0.2, anchor="center")

    start_button = tk.Button(root, text="Start", command=open_menu, font=("Helvetica", 14, "bold"), bg="#3CB371", width=15, padx=10, pady=5)
    start_button.place(relx=0.5, rely=0.5, anchor="center")

    exit_button = tk.Button(root, text="Exit", command=root.destroy, font=("Helvetica", 14, "bold"), bg="#FF6347", width=15, padx=10, pady=5)
    exit_button.place(relx=0.5, rely=0.6, anchor="center")

    root.mainloop()

def open_menu():
    menu_window = tk.Toplevel()
    menu_window.title("Menu")
    menu_window.geometry("400x300")
    menu_window.config(bg="#2c3e50")  # Set background color to dark blue

    menu_frame = tk.Frame(menu_window, bg="#3c3e50")
    menu_frame.place(relx=0.5, rely=0.5, anchor="center")

    employee_button = tk.Button(menu_frame, text="Employee", command=lambda: open_employee_menu(Employee), font=("Helvetica", 12, "bold"), bg="#3498db", fg="black", width=15, padx=10, pady=5)
    employee_button.grid(row=0, column=0, pady=5)

    client_button = tk.Button(menu_frame, text="Client", command=lambda: open_client_menu(Client), font=("Helvetica", 12, "bold"), bg="#e74c3c", fg="black", width=15, padx=10, pady=5)
    client_button.grid(row=1, column=0, pady=5)

    venue_button = tk.Button(menu_frame, text="Venue", command=lambda: open_venue_menu(Venue), font=("Helvetica", 12, "bold"), bg="#2ecc71", fg="black", width=15, padx=10, pady=5)
    venue_button.grid(row=2, column=0, pady=5)

    guest_button = tk.Button(menu_frame, text="Guest", command=lambda: open_guest_menu(Guest), font=("Helvetica", 12, "bold"), bg="#f39c12", fg="black", width=15, padx=10, pady=5)
    guest_button.grid(row=3, column=0, pady=5)

    supplier_button = tk.Button(menu_frame, text="Supplier", command=lambda: open_supplier_menu(Supplier), font=("Helvetica", 12, "bold"), bg="#9b59b6", fg="black", width=15, padx=10, pady=5)
    supplier_button.grid(row=4, column=0, pady=5)

    event_button = tk.Button(menu_frame, text="Event", command=lambda: open_event_menu(Event), font=("Helvetica", 12, "bold"), bg="pink", fg="black", width=15, padx=10, pady=5)
    event_button.grid(row=5, column=0, pady=5)

def open_employee_menu(Employee):
    employee_window = tk.Toplevel()
    employee_window.title("Employee Menu")

    # Set background color
    employee_window.config(bg="#2c3e50")

    # Increase the size of the window
    employee_window.geometry("300x300")

    # Create a frame to organize buttons
    menu_frame = tk.Frame(employee_window, bg="#3c3e50")
    menu_frame.pack(pady=30)

    # Define button widths
    add_button_width = 18
    edit_button_width = 18
    del_button_width = 18
    display_button_width = 18

    # Add button for each operation
    add_button = tk.Button(menu_frame, text="Add", command=Employee.add, font=("Helvetica", 12, "bold"), bg="yellow", fg="black", width=add_button_width, pady=5)
    add_button.pack()

    edit_button = tk.Button(menu_frame, text="Edit", command=Employee.edit, font=("Helvetica", 12, "bold"), bg="pink", fg="black", width=edit_button_width, pady=5)
    edit_button.pack()

    del_button = tk.Button(menu_frame, text="Delete", command=Employee.delete, font=("Helvetica", 12, "bold"), bg="green", fg="black", width=del_button_width, pady=5)
    del_button.pack()

    display_button = tk.Button(menu_frame, text="Display", command=Employee.display, font=("Helvetica", 12, "bold"), bg="orange", fg="black", width=display_button_width, pady=5)
    display_button.pack()

def open_client_menu(Client):
    client_window = tk.Toplevel()
    client_window.title("Client Menu")

    # Set background color
    client_window.config(bg="#2c3e50")

    # Increase the size of the window
    client_window.geometry("300x300")

    # Create a frame to organize buttons
    menu_frame = tk.Frame(client_window, bg="#3c3e50")
    menu_frame.pack(pady=30)

    # Define button widths
    button_width = 18

    # Add buttons for each operation
    add_button = tk.Button(menu_frame, text="Add", command=Client.add, font=("Helvetica", 12, "bold"), bg="yellow", fg="black", width=button_width, pady=5)
    add_button.pack()

    edit_button = tk.Button(menu_frame, text="Edit", command=Client.edit, font=("Helvetica", 12, "bold"), bg="pink", fg="black", width=button_width, pady=5)
    edit_button.pack()

    del_button = tk.Button(menu_frame, text="Delete", command=Client.delete, font=("Helvetica", 12, "bold"), bg="green", fg="black", width=button_width, pady=5)
    del_button.pack()

    display_button = tk.Button(menu_frame, text="Display", command=Client.display, font=("Helvetica", 12, "bold"), bg="orange", fg="black", width=button_width, pady=5)
    display_button.pack()

def open_event_menu(Event):
    event_window = tk.Toplevel()
    event_window.title("Event Menu")

    # Set background color
    event_window.config(bg="#2c3e50")

    # Increase the size of the window
    event_window.geometry("300x300")

    # Create a frame to organize buttons
    menu_frame = tk.Frame(event_window, bg="#3c3e50")
    menu_frame.pack(pady=30)

    # Define button widths
    button_width = 18

    # Add buttons for each operation
    add_button = tk.Button(menu_frame, text="Add", command=Event.add, font=("Helvetica", 12, "bold"), bg="yellow", fg="black", width=button_width, pady=5)
    add_button.pack()

    edit_button = tk.Button(menu_frame, text="Edit", command=Event.edit, font=("Helvetica", 12, "bold"), bg="pink", fg="black", width=button_width, pady=5)
    edit_button.pack()

    del_button = tk.Button(menu_frame, text="Delete", command=Event.delete, font=("Helvetica", 12, "bold"), bg="green", fg="black", width=button_width, pady=5)
    del_button.pack()

    display_button = tk.Button(menu_frame, text="Display", command=Event.display, font=("Helvetica", 12, "bold"), bg="orange", fg="black", width=button_width, pady=5)
    display_button.pack()

def open_guest_menu(Guest):
    guest_window = tk.Toplevel()
    guest_window.title("Guest Menu")

    # Set background color
    guest_window.config(bg="#2c3e50")

    # Increase the size of the window
    guest_window.geometry("300x300")

    # Create a frame to organize buttons
    menu_frame = tk.Frame(guest_window, bg="#3c3e50")
    menu_frame.pack(pady=30)

    # Define button widths
    button_width = 18

    # Add buttons for each operation
    add_button = tk.Button(menu_frame, text="Add", command=Guest.add, font=("Helvetica", 12, "bold"), bg="yellow", fg="black", width=button_width, pady=5)
    add_button.pack()

    edit_button = tk.Button(menu_frame, text="Edit", command=Guest.edit, font=("Helvetica", 12, "bold"), bg="pink", fg="black", width=button_width, pady=5)
    edit_button.pack()

    del_button = tk.Button(menu_frame, text="Delete", command=Guest.delete, font=("Helvetica", 12, "bold"), bg="green", fg="black", width=button_width, pady=5)
    del_button.pack()

    display_button = tk.Button(menu_frame, text="Display", command=Guest.display, font=("Helvetica", 12, "bold"), bg="orange", fg="black", width=button_width, pady=5)
    display_button.pack()

def open_supplier_menu(Supplier):
    supplier_window = tk.Toplevel()
    supplier_window.title("Supplier Menu")

    # Set background color
    supplier_window.config(bg="#2c3e50")

    # Increase the size of the window
    supplier_window.geometry("300x300")

    # Create a frame to organize buttons
    menu_frame = tk.Frame(supplier_window, bg="#3c3e50")
    menu_frame.pack(pady=30)

    # Define button widths
    button_width = 18

    # Add buttons for each operation
    add_button = tk.Button(menu_frame, text="Add", command=Supplier.add, font=("Helvetica", 12, "bold"), bg="yellow", fg="black", width=button_width, pady=5)
    add_button.pack()

    edit_button = tk.Button(menu_frame, text="Edit", command=Supplier.edit, font=("Helvetica", 12, "bold"), bg="pink", fg="black", width=button_width, pady=5)
    edit_button.pack()

    del_button = tk.Button(menu_frame, text="Delete", command=Supplier.delete, font=("Helvetica", 12, "bold"), bg="green", fg="black", width=button_width, pady=5)
    del_button.pack()

    display_button = tk.Button(menu_frame, text="Display", command=Supplier.display, font=("Helvetica", 12, "bold"), bg="orange", fg="black", width=button_width, pady=5)
    display_button.pack()

def open_venue_menu(Venue):
    venue_window = tk.Toplevel()
    venue_window.title("Venue Menu")

    # Set background color
    venue_window.config(bg="#2c3e50")

    # Increase the size of the window
    venue_window.geometry("300x300")

    # Create a frame to organize buttons
    menu_frame = tk.Frame(venue_window, bg="#3c3e50")
    menu_frame.pack(pady=30)

    # Define button widths
    button_width = 18

    # Add buttons for each operation
    add_button = tk.Button(menu_frame, text="Add", command=Venue.add, font=("Helvetica", 12, "bold"), bg="yellow", fg="black", width=button_width, pady=5)
    add_button.pack()

    edit_button = tk.Button(menu_frame, text="Edit", command=Venue.edit, font=("Helvetica", 12, "bold"), bg="pink", fg="black", width=button_width, pady=5)
    edit_button.pack()

    del_button = tk.Button(menu_frame, text="Delete", command=Venue.delete, font=("Helvetica", 12, "bold"), bg="green", fg="black", width=button_width, pady=5)
    del_button.pack()

    display_button = tk.Button(menu_frame, text="Display", command=Venue.display, font=("Helvetica", 12, "bold"), bg="orange", fg="black", width=button_width, pady=5)
    display_button.pack()

if __name__ == "__main__":
    main()
