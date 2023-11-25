import pandas as pd

def track_efficiency():
    # Assuming you have a CSV file named 'employees.csv' with columns: employee_id, efficiency_rating
    file_path = 'employees.csv'

    try:
        # Load the existing data from the CSV file
        df = pd.read_csv(file_path)

        # Display the current efficiency ratings
        print("Current Efficiency Ratings:")
        print(df[['employee_id', 'efficiency_rating']])

        # Prompt user to update efficiency for existing employees
        while True:
            employee_id = input("Enter Employee ID to update efficiency (or type 'done' to finish): ")

            if employee_id.lower() == 'done':
                break

            employee_id = int(employee_id)
            if employee_id in df['employee_id'].values:
                efficiency_rating = float(input(f"Enter new efficiency rating for Employee {employee_id}: "))
                df.loc[df['employee_id'] == employee_id, 'efficiency_rating'] = efficiency_rating
                print(f"Efficiency rating for Employee {employee_id} updated.")
            else:
                print(f"Employee {employee_id} not found.")

        # Save the updated DataFrame back to the CSV file
        df.to_csv(file_path, index=False)

    except ValueError:
        print("Invalid input. Please enter valid numeric values.")
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except pd.errors.EmptyDataError:
        print(f"File '{file_path}' is empty.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Uncomment the line below if you want to execute the function
# track_efficiency()
