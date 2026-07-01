class Employee:

    def __init__(self, emp_id, name, age, department):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.department = department


employees = []
        
def add_employee():

    emp_id = input("Enter Employee ID: ")
    name = input("Enter Name: ")
    age = input("Enter Age: ")
    department = input("Enter Department: ")

    employee = Employee(emp_id, name, age, department)

    employees.append(employee)

    print("\nEmployee added successfully!\n")
    
def view_employees():

    if len(employees) == 0:
        print("\nNo employees found.\n")
        return

    print("\nEmployee List")

    for employee in employees:
        print("--------------------------")
        print("ID:", employee.emp_id)
        print("Name:", employee.name)
        print("Age:", employee.age)
        print("Department:", employee.department)
        
def update_employee():

    emp_id = input("Enter Employee ID to update: ")

    for employee in employees:

        if employee.emp_id == emp_id:

            employee.name = input("Enter New Name: ")
            employee.age = input("Enter New Age: ")
            employee.department = input("Enter New Department: ")

            print("\nEmployee updated successfully!\n")
            return

    print("\nEmployee not found!\n")
    
def delete_employee():

    emp_id = input("Enter Employee ID to delete: ")

    for employee in employees:

        if employee.emp_id == emp_id:

            employees.remove(employee)

            print("\nEmployee deleted successfully!\n")

            return

    print("\nEmployee not found!\n")
        
while True:

    print("\n===== Employee Management System =====")
    print("1. Add Employee")
    print("2. View Employees")
    print("3. Update Employee")
    print("4. Delete Employee")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_employee()

    elif choice == "2":
        view_employees()

    elif choice == "3":
        update_employee()

    elif choice == "4":
        delete_employee()

    elif choice == "5":
        print("Thank you!")
        break

    else:
        print("Invalid choice!")
        
import json

