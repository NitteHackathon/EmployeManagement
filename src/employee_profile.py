
import pandas as pd

def update_employee_profile(employee_id, first_name, last_name, email, department):
    file_path = '/data/employees.csv'

    try:
        # Load the existing data from the CSV file
        df = pd.read_csv(file_path)

        # Check if the employee ID exists in the DataFrame
        if employee_id in df['employee_id'].values:
            # Display options for updating
            print("\nSelect the information to update:")
            print("1. First Name\n2. Last Name\n3. Email\n4. Department")
            choice = input("Enter your choice (comma-separated for multiple updates): ")

            update_choices = [int(x.strip()) for x in choice.split(',')]
            
            for update_choice in update_choices:
                if update_choice == 1:
                    df.loc[df['employee_id'] == employee_id, 'first_name'] = input("Enter new First Name: ")
                elif update_choice == 2:
                    df.loc[df['employee_id'] == employee_id, 'last_name'] = input("Enter new Last Name: ")
                elif update_choice == 3:
                    df.loc[df['employee_id'] == employee_id, 'email'] = input("Enter new Email: ")
                elif update_choice == 4:
                    df.loc[df['employee_id'] == employee_id, 'department'] = input("Enter new Department: ")

            # Save the updated DataFrame back to the CSV file
            df.to_csv(file_path, index=False)

            print(f"\nEmployee profile updated for {employee_id}.")

        else:
            print(f"\nEmployee with ID {employee_id} not found.")

    except FileNotFoundError:
        print(f"\nFile '{file_path}' not found.")
    except pd.errors.EmptyDataError:
        print(f"\nFile '{file_path}' is empty.")
    except Exception as e:
        print(f"\nAn error occurred: {e}")
