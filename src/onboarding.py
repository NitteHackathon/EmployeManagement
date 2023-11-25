import tkinter as tk
from tkinter import simpledialog
import pandas as pd

def onboard_employee(employee_id, first_name, last_name, email, department):
    file_path = 'employees.csv'

    try:
        # Load the existing data from the CSV file
        try:
            df = pd.read_csv(file_path)
        except FileNotFoundError:
            # If the file does not exist, create an empty DataFrame
            df = pd.DataFrame(columns=['employee_id', 'first_name', 'last_name', 'email', 'department'])

        # Check if the employee ID already exists
        if employee_id in df['employee_id'].values:
            print(f"Employee with ID {employee_id} already exists.")
        else:
            # Use a larger and more professional-looking dialogue box for input
            root = tk.Tk()
            root.withdraw()  # Hide the main window
            root.geometry("400x150")  # Set the size of the dialogue box
            root.title("Onboard Employee")

            email = simpledialog.askstring("Onboard Employee", "Enter Email:", parent=root)
            department = simpledialog.askstring("Onboard Employee", "Enter Department:", parent=root)

            root.destroy()  # Destroy the temporary window

            # Create a new DataFrame with the onboarded employee
            new_employee = pd.DataFrame({'employee_id': [employee_id],
                                          'first_name': [first_name],
                                          'last_name': [last_name],
                                          'email': [email],
                                          'department': [department]})

            # Concatenate the existing DataFrame with the new DataFrame
            frames = [df, new_employee]
            df = pd.concat(frames, ignore_index=True)

            # Save the updated DataFrame back to the CSV file
            df.to_csv(file_path, index=False)

            print(f"Employee onboarded successfully: {first_name} {last_name}, Email: {email}, Department: {department}")

    except Exception as e:
        print(f"An error occurred during onboarding: {e}")
