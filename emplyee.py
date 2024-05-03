import tkinter as tk
from tkinter import messagebox
import pickle


class Employee:
    def __init__(self, name, employee_id, department, job_title, basic_salary, age, dob, passport_details,
                 manager_id=None):
        self.name = name
        self.employee_id = employee_id
        self.department = department
        self.job_title = job_title
        self.basic_salary = basic_salary
        self.age = age
        self.dob = dob
        self.passport_details = passport_details
        self.manager_id = manager_id

    @staticmethod
    def add():
        add_employee_window = tk.Toplevel()
        add_employee_window.title("Add Employee")

        # Set background color
        add_employee_window.config(bg="#2c3e50")

        # Create a frame to organize entries and labels
        entry_frame = tk.Frame(add_employee_window, bg="#2c3e50")
        entry_frame.pack(pady=20)

        # Define label width
        label_width = 15

        # Create labels and entry fields
        tk.Label(entry_frame, text="Name:", bg="#2c3e50", fg="white", width=label_width).grid(row=0, column=0, padx=10,
                                                                                              pady=5)
        name_entry = tk.Entry(entry_frame)
        name_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(entry_frame, text="Employee ID:", bg="#2c3e50", fg="white", width=label_width).grid(row=1, column=0,
                                                                                                     padx=10, pady=5)
        employee_id_entry = tk.Entry(entry_frame)
        employee_id_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(entry_frame, text="Department:", bg="#2c3e50", fg="white", width=label_width).grid(row=2, column=0,
                                                                                                    padx=10, pady=5)
        department_entry = tk.Entry(entry_frame)
        department_entry.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(entry_frame, text="Job Title:", bg="#2c3e50", fg="white", width=label_width).grid(row=3, column=0,
                                                                                                   padx=10, pady=5)
        job_title_entry = tk.Entry(entry_frame)
        job_title_entry.grid(row=3, column=1, padx=10, pady=5)

        tk.Label(entry_frame, text="Basic Salary:", bg="#2c3e50", fg="white", width=label_width).grid(row=4, column=0,
                                                                                                      padx=10, pady=5)
        basic_salary_entry = tk.Entry(entry_frame)
        basic_salary_entry.grid(row=4, column=1, padx=10, pady=5)

        tk.Label(entry_frame, text="Age:", bg="#2c3e50", fg="white", width=label_width).grid(row=5, column=0, padx=10,
                                                                                             pady=5)
        age_entry = tk.Entry(entry_frame)
        age_entry.grid(row=5, column=1, padx=10, pady=5)

        tk.Label(entry_frame, text="Date of Birth:", bg="#2c3e50", fg="white", width=label_width).grid(row=6, column=0,
                                                                                                       padx=10, pady=5)
        dob_entry = tk.Entry(entry_frame)
        dob_entry.grid(row=6, column=1, padx=10, pady=5)

        tk.Label(entry_frame, text="Passport Details:", bg="#2c3e50", fg="white", width=label_width).grid(row=7,
                                                                                                          column=0,
                                                                                                          padx=10,
                                                                                                          pady=5)
        passport_details_entry = tk.Entry(entry_frame)
        passport_details_entry.grid(row=7, column=1, padx=10, pady=5)

        # Save button
        save_button = tk.Button(add_employee_window, text="Save", command=lambda: save_employee(
            name_entry, employee_id_entry, department_entry, job_title_entry, basic_salary_entry, age_entry, dob_entry,
            passport_details_entry), bg="green", fg="white")
        save_button.pack(pady=10)

    @staticmethod
    def edit():
        # Create a window to take employee ID input for editing
        edit_window = tk.Toplevel()
        edit_window.title("Edit Employee")
        edit_window.config(bg="#2c3e50")

        # Create label and entry for Employee ID
        tk.Label(edit_window, text="Enter Employee ID to edit:", bg="#2c3e50", fg="white").pack(pady=10)
        employee_id_entry = tk.Entry(edit_window)
        employee_id_entry.pack(pady=5)

        # Define function to edit employee
        def edit_employee():
            emp_id = employee_id_entry.get()
            with open("binary_emp.pkl", "rb") as file:
                serialized_employee = file.read()
                employee_data = pickle.loads(serialized_employee)

            if 'Employee ID' in employee_data and employee_data['Employee ID'] == emp_id:
                # Open a new window to edit employee details
                edit_employee_window = tk.Toplevel()
                edit_employee_window.title("Edit Employee Details")
                edit_employee_window.config(bg="#2c3e50")

                # Create a frame to organize entries and labels
                entry_frame = tk.Frame(edit_employee_window, bg="#2c3e50")
                entry_frame.pack(pady=20)

                # Define label width
                label_width = 15

                # Create labels and entry fields
                tk.Label(entry_frame, text="Name:", bg="#2c3e50", fg="white", width=label_width).grid(row=0, column=0,
                                                                                                      padx=10, pady=5)
                name_entry = tk.Entry(entry_frame)
                name_entry.insert(0, employee_data['Name'])  # Fill current name
                name_entry.grid(row=0, column=1, padx=10, pady=5)

                tk.Label(entry_frame, text="Department:", bg="#2c3e50", fg="white", width=label_width).grid(row=1,
                                                                                                            column=0,
                                                                                                            padx=10,
                                                                                                            pady=5)
                department_entry = tk.Entry(entry_frame)
                department_entry.insert(0, employee_data['Department'])  # Fill current department
                department_entry.grid(row=1, column=1, padx=10, pady=5)

                tk.Label(entry_frame, text="Job Title:", bg="#2c3e50", fg="white", width=label_width).grid(row=2,
                                                                                                           column=0,
                                                                                                           padx=10,
                                                                                                           pady=5)
                job_title_entry = tk.Entry(entry_frame)
                job_title_entry.insert(0, employee_data['Job Title'])  # Fill current job title
                job_title_entry.grid(row=2, column=1, padx=10, pady=5)

                tk.Label(entry_frame, text="Basic Salary:", bg="#2c3e50", fg="white", width=label_width).grid(row=3,
                                                                                                              column=0,
                                                                                                              padx=10,
                                                                                                              pady=5)
                basic_salary_entry = tk.Entry(entry_frame)
                basic_salary_entry.insert(0, employee_data['Basic Salary'])  # Fill current basic salary
                basic_salary_entry.grid(row=3, column=1, padx=10, pady=5)

                tk.Label(entry_frame, text="Age:", bg="#2c3e50", fg="white", width=label_width).grid(row=4, column=0,
                                                                                                     padx=10, pady=5)
                age_entry = tk.Entry(entry_frame)
                age_entry.insert(0, employee_data['Age'])  # Fill current age
                age_entry.grid(row=4, column=1, padx=10, pady=5)

                tk.Label(entry_frame, text="Date of Birth:", bg="#2c3e50", fg="white", width=label_width).grid(row=5,
                                                                                                               column=0,
                                                                                                               padx=10,
                                                                                                               pady=5)
                dob_entry = tk.Entry(entry_frame)
                dob_entry.insert(0, employee_data['Date of Birth'])  # Fill current date of birth
                dob_entry.grid(row=5, column=1, padx=10, pady=5)

                tk.Label(entry_frame, text="Passport Details:", bg="#2c3e50", fg="white", width=label_width).grid(row=6,
                                                                                                                  column=0,
                                                                                                                  padx=10,
                                                                                                                  pady=5)
                passport_details_entry = tk.Entry(entry_frame)
                passport_details_entry.insert(0, employee_data['Passport Details'])  # Fill current passport details
                passport_details_entry.grid(row=6, column=1, padx=10, pady=5)

                # Save button to update employee details
                save_button = tk.Button(edit_employee_window, text="Update", command=lambda: update_employee(
                    emp_id, name_entry, department_entry, job_title_entry, basic_salary_entry, age_entry, dob_entry,
                    passport_details_entry), bg="green", fg="white")
                save_button.pack(pady=10)
            else:
                messagebox.showerror("Error", "Employee ID not found or does not match.")

        # Create button to confirm editing
        edit_button = tk.Button(edit_window, text="Edit", command=edit_employee, bg="orange", fg="white")
        edit_button.pack(pady=10)

    @staticmethod
    def delete():
        # Create a window to take employee ID input for deletion
        delete_window = tk.Toplevel()
        delete_window.title("Delete Employee")
        delete_window.config(bg="#2c3e50")

        # Create label and entry for Employee ID
        tk.Label(delete_window, text="Enter Employee ID to delete:", bg="#2c3e50", fg="white").pack(pady=10)
        employee_id_entry = tk.Entry(delete_window)
        employee_id_entry.pack(pady=5)

        # Define function to delete employee
        def delete_employee():
            emp_id = employee_id_entry.get()
            with open("binary_emp.pkl", "rb") as file:
                serialized_employee = file.read()
                employee_data = pickle.loads(serialized_employee)

            if 'Employee ID' in employee_data and employee_data['Employee ID'] == emp_id:
                del employee_data['Employee ID']  # Delete the employee entry
                with open("binary_emp.pkl", "wb") as file:
                    pickle.dump(employee_data, file)  # Write updated data back to file
                messagebox.showinfo("Success", "Employee deleted successfully.")
            else:
                messagebox.showerror("Error", "Employee ID not found or does not match.")

        # Create button to confirm deletion
        delete_button = tk.Button(delete_window, text="Delete", command=delete_employee, bg="red", fg="white")
        delete_button.pack(pady=10)

    @staticmethod
    def display():
        display_window = tk.Toplevel()
        display_window.title("Employee Details")
        display_window.config(bg="#2c3e50")
        entry_frame = tk.Frame(display_window, bg="#2c3e50")
        entry_frame.pack(pady=20)
        label_width = 15

        employee_id_label = tk.Label(entry_frame, text="Enter Employee ID:", bg="#2c3e50", fg="white",
                                     width=label_width)
        employee_id_label.grid(row=0, column=0, padx=10, pady=5)
        employee_id_entry = tk.Entry(entry_frame)
        employee_id_entry.grid(row=0, column=1, padx=10, pady=5)

        search_button = tk.Button(entry_frame, text="Search", command=lambda: search_employee(employee_id_entry),
                                  bg="blue", fg="white")
        search_button.grid(row=1, columnspan=2, pady=10)

        def search_employee(entry):
            # Retrieve data from pickle file
            with open("binary_emp.pkl", "rb") as file:
                serialized_employee = file.read()
                employee_data = pickle.loads(serialized_employee)

            emp_id = entry.get()

            if 'Employee ID' in employee_data and employee_data['Employee ID'] == emp_id:
                display_employee_details(employee_data)
            else:
                messagebox.showerror("Error", "Employee ID not found.")

        def display_employee_details(employee_details):
            display_frame = tk.Frame(display_window, bg="#2c3e50")
            display_frame.pack(pady=20)

            for i, (key, value) in enumerate(employee_details.items()):
                tk.Label(display_frame, text=key + ":", bg="#2c3e50", fg="white", width=label_width).grid(row=i,
                                                                                                          column=0,
                                                                                                          padx=10,
                                                                                                          pady=5)
                tk.Label(display_frame, text=value, bg="#2c3e50", fg="white").grid(row=i, column=1, padx=10, pady=5)


def save_employee(name_entry, employee_id_entry, department_entry, job_title_entry, basic_salary_entry, age_entry,
                  dob_entry, passport_details_entry):
    # Retrieve data from entry fields
    name = name_entry.get()
    employee_id = employee_id_entry.get()
    department = department_entry.get()
    job_title = job_title_entry.get()
    basic_salary = basic_salary_entry.get()
    age = age_entry.get()
    dob = dob_entry.get()
    passport_details = passport_details_entry.get()

    # Create a dictionary to store employee data
    employee_data = {
        "Name": name,
        "Employee ID": employee_id,
        "Department": department,
        "Job Title": job_title,
        "Basic Salary": basic_salary,
        "Age": age,
        "Date of Birth": dob,
        "Passport Details": passport_details
    }

    # Serialize the dictionary object
    serialized_employee = pickle.dumps(employee_data)

    # Write the serialized data to the pickle file
    with open("binary_emp.pkl", "wb") as file:
        file.write(serialized_employee)

    messagebox.showinfo("Success", "Employee added successfully.")


def update_employee(emp_id, name_entry, department_entry, job_title_entry, basic_salary_entry, age_entry, dob_entry,
                    passport_details_entry):
    # Retrieve data from entry fields
    name = name_entry.get()
    department = department_entry.get()
    job_title = job_title_entry.get()
    basic_salary = basic_salary_entry.get()
    age = age_entry.get()
    dob = dob_entry.get()
    passport_details = passport_details_entry.get()

    # Create a dictionary to store updated employee data
    updated_employee_data = {
        "Name": name,
        "Employee ID": emp_id,
        "Department": department,
        "Job Title": job_title,
        "Basic Salary": basic_salary,
        "Age": age,
        "Date of Birth": dob,
        "Passport Details": passport_details
    }

    # Serialize the updated dictionary object
    serialized_updated_employee = pickle.dumps(updated_employee_data)

    # Write the serialized data to the pickle file
    with open("binary_emp.pkl", "wb") as file:
        file.write(serialized_updated_employee)

    messagebox.showinfo("Success", "Employee details updated successfully.")
