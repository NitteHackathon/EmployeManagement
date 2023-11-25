import tkinter as tk
from tkinter import ttk, simpledialog
import pandas as pd

from onboarding import onboard_employee
from employee_profile import update_employee_profile
from salary_calculations import calculate_salary
from efficiency_tracking import track_efficiency

class WorkforceManagementApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Workforce Management System")

        # Style for ttk
        style = ttk.Style()
        style.configure("TFrame", background="#f0f0f0")
        style.configure("TLabel", background="#f0f0f0")
        style.configure("TRadiobutton", background="#f0f0f0")
        style.configure("TButton", background="#4CAF50", foreground="white")
        style.configure("TEntry", padding=(5, 5))

        self.menu_frame = ttk.Frame(self.root, padding=(10, 10), style="TFrame")
        self.menu_frame.grid(row=0, column=0)

        self.choice_label = ttk.Label(self.menu_frame, text="Choose an action:", style="TLabel")
        self.choice_label.grid(row=0, column=0, columnspan=2, pady=10, sticky="w")

        self.choice_var = tk.StringVar()
        self.choice_var.set("1")

        self.choices = [("Onboard Employee", "1"),
                        ("Update Employee Profile", "2"),
                        ("Calculate Salary", "3"),
                        ("Track Efficiency", "4"),
                        ("Exit", "5")]

        for i, (text, value) in enumerate(self.choices, start=1):
            ttk.Radiobutton(self.menu_frame, text=text, variable=self.choice_var, value=value, style="TRadiobutton").grid(
                row=i, column=0, columnspan=2, sticky="w", pady=5)

        self.employee_id_label = ttk.Label(self.menu_frame, text="Enter Employee ID:", style="TLabel")
        self.employee_id_label.grid(row=len(self.choices) + 1, column=0, columnspan=2, pady=10, sticky="w")

        self.employee_id_entry = ttk.Entry(self.menu_frame, style="TEntry")
        self.employee_id_entry.grid(row=len(self.choices) + 2, column=0, columnspan=2, pady=10, sticky="ew")

        self.first_name_label = ttk.Label(self.menu_frame, text="Enter First Name:", style="TLabel")
        self.first_name_label.grid(row=len(self.choices) + 3, column=0, columnspan=2, pady=10, sticky="w")

        self.first_name_entry = ttk.Entry(self.menu_frame, style="TEntry")
        self.first_name_entry.grid(row=len(self.choices) + 4, column=0, columnspan=2, pady=10, sticky="ew")

        self.last_name_label = ttk.Label(self.menu_frame, text="Enter Last Name:", style="TLabel")
        self.last_name_label.grid(row=len(self.choices) + 5, column=0, columnspan=2, pady=10, sticky="w")

        self.last_name_entry = ttk.Entry(self.menu_frame, style="TEntry")
        self.last_name_entry.grid(row=len(self.choices) + 6, column=0, columnspan=2, pady=10, sticky="ew")

        # Status message label
        self.status_label = ttk.Label(self.menu_frame, text="", style="TLabel")
        self.status_label.grid(row=len(self.choices) + 8, column=0, columnspan=2, pady=10, sticky="w")

        # Output Text widget
        self.output_text = tk.Text(self.root, wrap=tk.WORD, height=10, width=50)
        self.output_text.grid(row=1, column=1, padx=10, pady=10)

        self.submit_button = ttk.Button(self.menu_frame, text="Submit", command=self.handle_choice, style="TButton")
        self.submit_button.grid(row=len(self.choices) + 7, column=0, columnspan=2, pady=10)

        # Tooltips
        self.add_tooltips()

    def add_tooltips(self):
        tooltips = {
            "Enter Employee ID": "Please enter the unique ID of the employee.",
            "Enter First Name": "Please enter the first name of the employee.",
            "Enter Last Name": "Please enter the last name of the employee.",
        }

        for widget, tip in tooltips.items():
            widget_obj = getattr(self, f"{widget.lower().replace(' ', '_')}_entry", None)
            if widget_obj:
                widget_obj.bind("<Enter>", lambda event, tip=tip: self.show_tooltip(event, tip))
                widget_obj.bind("<Leave>", lambda event: self.hide_tooltip())

    def show_tooltip(self, event, text):
        self.status_label.configure(text=text)

    def hide_tooltip(self):
        self.status_label.configure(text="")

    def handle_choice(self):
        choice = self.choice_var.get()
        employee_id = self.employee_id_entry.get()
        first_name = self.first_name_entry.get()
        last_name = self.last_name_entry.get()

        try:
            if choice == '1':
                email = simpledialog.askstring("Input", "Enter Email:")
                department = simpledialog.askstring("Input", "Enter Department:")
                result = onboard_employee(employee_id, first_name, last_name, email, department)
            elif choice == '2':
                email = simpledialog.askstring("Input", "Enter Email:")
                department = simpledialog.askstring("Input", "Enter Department:")
                result = update_employee_profile(employee_id, first_name, last_name, email, department)
            elif choice == '3':
                salary = simpledialog.askstring("Input", "Enter Salary:")
                result = calculate_salary(employee_id, salary)
            elif choice == '4':
                efficiency_rating = simpledialog.askstring("Input", "Enter Efficiency Rating:")
                result = track_efficiency(employee_id, efficiency_rating)
            elif choice == '5':
                result = "Exiting..."
                self.root.destroy()
            else:
                result = "Invalid choice. Please try again."

            # Display the result in the Text widget
            self.output_text.insert(tk.END, str(result) + "\n")


        except Exception as e:
            print(f"An error occurred: {e}")
            self.output_text.insert(tk.END, f"An error occurred: {e}\n")

def main():
    root = tk.Tk()
    app = WorkforceManagementApp(root)
    root.eval('tk::PlaceWindow . center')
    root.mainloop()

if __name__ == "__main__":
    main()
