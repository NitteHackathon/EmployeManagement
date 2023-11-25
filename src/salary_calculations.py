import pandas as pd

def calculate_salary():
    # Assuming you have a CSV file named 'employees.csv' with columns: employee_id, salary, bonus_percentage
    file_path = 'employees.csv'

    try:
        # Load the existing data from the CSV file
        df = pd.read_csv(file_path)

        # Display the current salary information
        print("Current Salary Information:")
        print(df[['employee_id', 'salary', 'bonus_percentage']])

        # Prompt user to update salary for existing employees
        while True:
            employee_id = input("Enter Employee ID to update salary (or type 'done' to finish): ")

            if employee_id.lower() == 'done':
                break

            employee_id = int(employee_id)
            if employee_id in df['employee_id'].values:
                # Prompt user to enter the new salary
                new_salary = float(input(f"Enter new salary for Employee {employee_id}: "))
                df.loc[df['employee_id'] == employee_id, 'salary'] = new_salary

                # Assuming the bonus is calculated based on a percentage of the new salary
                bonus_percentage = float(input(f"Enter bonus percentage for Employee {employee_id}: "))
                df.loc[df['employee_id'] == employee_id, 'bonus_percentage'] = bonus_percentage

                # Calculate bonus and total salary
                df['bonus'] = df['salary'] * (df['bonus_percentage'] / 100)
                df['total_salary'] = df['salary'] + df['bonus']

                print(f"Salary update for Employee {employee_id} completed.")
            else:
                print(f"Employee {employee_id} not found.")

        # Save the updated DataFrame back to the CSV file
        df.to_csv(file_path, index=False)

        print("Changes saved to the CSV file.")

    except ValueError:
        print("Invalid input. Please enter valid numeric values.")
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except pd.errors.EmptyDataError:
        print(f"File '{file_path}' is empty.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Uncomment the line below if you want to execute the function
# calculate_salary()
