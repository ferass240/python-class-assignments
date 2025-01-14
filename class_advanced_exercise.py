class Employee:

    def __init__(self, emp_id, name, position, salary, projects):
        self.emp_id = emp_id
        self.name = name
        self.position = position
        self.salary = salary
        self.projects = projects

    def display_emp_details(self):
        print(f"id: {self.emp_id}\t name: {self.name}\t position: {self.position}\t \
              salary: {self.salary}\t projects: {self.projects}")

    def update_position(self, position):
        self.position = position

    def update_salary(self, salary):
        self.salary = salary

    def assign_project(self, project):
        self.projects = project


class EmployeeManager:

    def __init__(self, list_employees):
        self.list_employees = list_employees

    def add_employee(self):
        print("Enter details for the employee:\n")
        emp_id = int(input("ID:\n"))
        name = input("Name:\n")
        position = input("Position:\n")
        salary = int(input("salary:\n"))
        projects = input("Projects(comma-separated):\n")

        emp = Employee(emp_id, "name", "position", salary, "projects")
        return emp

    def display_all_employees(self):
        for emp in self.list_employees:
            emp.display_emp_details()


    def search_emp_by_id(self, id):

        emp_found = next((emp for emp in self.list_employees if emp.emp_id == id),None)
        if emp_found:
            emp_found.display_emp_details()
            pass


while True:

    print(f"1. Add employee\n2.Display all employees\n3.Search for employee\n4. Update employee details\n5. Assign project to employee\n6. Calculate total salary\n7.List employees by project\n8. Exit")

    option = int(input("Please select an option: \n"))

    manager = EmployeeManager([])
    if option == 1:
        manager.add_employee()
    if option == 2:
        manager.display_all_employees()
    if option ==8:
        break