class Employee:

    def __init__(self, emp_id, name, position, salary, projects):
        self.emp_id = emp_id
        self.name = name
        self.position = position
        self.salary = salary
        self.projects = projects

    def display_emp_details(self):
        print(f"id: {self.emp_id}\t name: {self.name}\t position: {self.position}\t"
              f"salary: {self.salary}\t projects: {self.projects}")

    def update_position(self, position = None):
        if position:
            self.position = position
            print(f"position for employee {self.emp_id} updated.")

    def update_salary(self, salary = None):
        if salary:
            self.salary = salary
            print(f"Salary for employee {self.emp_id} updated.")


    def assign_project(self, project):
        project_found = next((proj for proj in self.projects if proj == "project"),None)
        if not project_found:
            self.projects.append(project)
        else:
            print(f"Project {project} is already assigned!")



class EmployeeManager:

    def __init__(self):
        self.list_employees = []

    def add_employee(self, employee):
        self.list_employees.append(employee)
        print(f"Employee {employee.emp_id} added")


    def display_all_employees(self):
        if not self.list_employees:
            print("No employees to display!")
        else:
            for emp in self.list_employees:
                emp.display_emp_details()


    def search_emp_by_id(self, emp_id):

        for emp in self.list_employees:
            if emp.emp_id == emp_id:
                #emp.display_emp_details()
                return emp
        print("employee does not exist!")
        return None

    def calculate_total_salary(self):
        if not self.list_employees:
            print("No employees yet. Please add new employee")
        total_salary = 0
        for emp in self.list_employees:
            total_salary += emp.salary
        print(f"Total Salary: {total_salary}")
        return total_salary

    def list_managers_projects(self, project):
        emp_found = next((emp for emp in self.list_employees if project in emp.projects),None)
        if emp_found:
            for emp in self.list_employees:
                if project in emp.projects:
                    emp.display_emp_details()
        else:
            print("No employee currently work on this project!")


def main():
    manager = EmployeeManager()
    while True:
        print(f"1. Add employee\n2.Display all employees\n3.Search for employee\n4. Update employee details\n5. Assign project to employee\n6. Calculate total salary\n7.List employees by project\n8. Exit")
        option = input("Please select an option: \n")

        if option == "1":
            print("Enter details for the employee:")
            emp_id = int(input("ID:"))
            name = input("Name:")
            position = input("Position:")
            salary = int(input("salary:"))
            projects_txt = input("Projects(comma-separated):")
            projects = projects_txt.split(",")

            emp = manager.search_emp_by_id(emp_id)
            if not emp:
                employee = Employee(emp_id, name, position, salary, projects)
                manager.add_employee(employee)
            else:
                print("This employee is already in the system!")

        if option == "2":
            manager.display_all_employees()

        if option == "3":
            emp_id = int(input("Enter employee ID:"))
            manager.search_emp_by_id(emp_id)
        if option == "4":

            emp_id = int(input("Enter employee ID:"))
            emp = manager.search_emp_by_id(emp_id)
            if emp:
                emp_pos = input("Enter new position (leave blank to keep current): ")
                emp_salary = int(input("Enter new salary (leave blank to keep current): "))
                emp.update_position(emp_pos)
                emp.update_salary(emp_salary)

        if option == "5":
            txt = input("Enter employee ID and project (comma-separated):")
            split_txt = txt.split(",")
            print(split_txt)
            emp = manager.search_emp_by_id(int(split_txt[0]))
            if emp:
                emp.assign_project(split_txt[1])
                emp.display_emp_details()

        if option == "6":
            manager.calculate_total_salary()
        if option =="7":
            proj = input("Enter project: ")
            manager.list_managers_projects(proj)
        if option =="8":
            break

        else:
            print("Invalid option. Please try again!")

if __name__ == "__main__":
    main()