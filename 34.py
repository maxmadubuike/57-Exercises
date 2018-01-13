'''
Exercise 34: Employee List Removal

Create a small program that contains a list of employee names.  Print out the
list of names when the program runs the first time.  Prompt the employee name
and remove that specific name from the list of names.  Display the remaining
employees, each on its own line.

Constraints:
Use an array or list to store the names.

'''

def greeting():
  print("Welcome to Exercise 34: Employee List Removal")
  
def main():
  greeting()
  employee_list = ["Isaac Asimov", "John Steinbeck", "George Orwell", "Sun Tzu", "Ray Bradbury"]
  print("There are {} employees:".format(len(employee_list)))
  for employee in employee_list:
    print(employee)
    
  employeeToRemove = input("Enter an employee name to remove: ")
  if employeeToRemove in employee_list:
    employee_list.remove(employeeToRemove)
    print("There are {} employees:".format(len(employee_list)))
    for employee in employee_list:
      print(employee)
  else:
    print("That person is not employed here.")
  
main()
