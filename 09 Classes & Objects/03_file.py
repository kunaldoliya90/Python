# 9.3
# Write a Python class Employee with attributes like emp_name, emp_id,
# emp_salary, emp_department and methods like calculate_salary, and
# print_details. Use 'calculate_salary' method takes two arguments: salary
# and hours_worked. If the number of hours worked is more than 50, the
# method computes overtime and adds it to the salary. Overtime is
# calculated as following formula:
# overtime = hours_worked – 50
# overtime amount = (overtime * (salary / 50))
# Use 'print_details' method to print the details of employee. Consider the
# sample data:
# "Adams " "E7876" 50000 "Accounting"
# "Jones" "E7499" 45000 "Research"
# "Martin" "E7900" 50000 "Sales"
# "Smith" "E7698" 55000 "Operations"

class Employee:
    def __init__(self, emp_name, emp_id, emp_salary, emp_department):
        self.emp_name = emp_name
        self.emp_id = emp_id
        self.emp_salary = emp_salary
        self.emp_department = emp_department

    def calculate_salary(self, hours_worked):
        if hours_worked > 50:
            overtime = hours_worked - 50
            overtime_amount = (overtime * (self.emp_salary / 50))
            total_salary = self.emp_salary + overtime_amount
        else:
            total_salary = self.emp_salary
        return total_salary

    def print_details(self):
        print("Employee Name:", self.emp_name)
        print("Employee ID:", self.emp_id)
        print("Employee Salary:", self.emp_salary)
        print("Employee Department:", self.emp_department)

# Sample data
employee1 = Employee("Adams", "E7876", 50000, "Accounting")
employee2 = Employee("Jones", "E7499", 45000, "Research")
employee3 = Employee("Martin", "E7900", 50000, "Sales")
employee4 = Employee("Smith", "E7698", 55000, "Operations")

# Example usage
print("Employee Details:")
employee1.print_details()
print("Total Salary (for 60 hours worked):", employee1.calculate_salary(60))
print()

employee2.print_details()
print("Total Salary (for 40 hours worked):", employee2.calculate_salary(40))
print()

employee3.print_details()
print("Total Salary (for 55 hours worked):", employee3.calculate_salary(55))
print()

employee4.print_details()
print("Total Salary (for 48 hours worked):", employee4.calculate_salary(48))
