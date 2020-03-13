#Name: Lawrence D'Addio
#Program Name: Employee Management System
#Date: 3/23/16
#Description: Program to keep track of employee objects, allows the user
#to update, delete, look up and add to a dictionary and then pickles the
#data to a file. 




import pickle
import employee

#Global constants for menu
LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5

#Global Constant for filename
FILENAME = 'employees.txt'



def main():

    #Loads existing contact dictionary and assigns it to employee_dct
    employee_dct = load_employees()

    choice = 0

    #Menu selection
    while choice != QUIT:

        #Gets choice
        choice = get_menu_choice()

        if choice == LOOK_UP:
            look_up(employee_dct)
        elif choice == ADD:
            add(employee_dct)
        elif choice == CHANGE:
            change(employee_dct)
        elif choice == DELETE:
            delete(employee_dct)

    #Save employee dictionary to file
    save_employees(employee_dct)


#Function to load data from a file and into a dictionary
def load_employees():
    try:
        #Open employees.txt file
        input_file = open(FILENAME, "rb")

        #Unpickle dictionary
        worker = pickle.load(input_file)

        #Close employees.txt file
        input_file.close()
        
    except EOFError:
        #Creates an empty dictionary if file cannot be opened
        worker = {}
       

    return worker


#Function to display menu and get validated choice
def get_menu_choice():

    print()
    print("Menu")
    print("____________________________")
    print("1. Look up employee")
    print("2. Add a new employee")
    print("3. Update an employee")
    print("4. Delete an employee")
    print("5. Quit the program")
    print()

    #Get the user's choice
    choice = int(input("Enter your choice: "))

    #Validate the choice.
    while choice < LOOK_UP or choice > QUIT:
        choice = int(input("Enter a valid choice: "))

    return choice


#Function that looks up an employee
def look_up(employee_dct):

    #Prompt to enter a name to look up
    id_num = input("Enter an id number: ")

    #Look up in dictionary
    print(employee_dct.get(id_num, "That ID number is not found."))



#Function to add to dictionary
def add(employee_dct):

    #Get employee information
    name = input("Name: ")
    id_num = input("ID Number: ")
    department = input("Department: ")
    job_title = input("Job Title: ")

    #Create a contact object named worker
    worker = employee.Employee(name, id_num, department, job_title)

    if id_num not in employee_dct:
        employee_dct[id_num] = worker
        print("The entry has been added.")
    else:
        print("That ID Number already exist.")



#Function to change an existing entry in a specified dictionary
def change(employee_dct):

    #Prompt for ID number to look up
    id_num = input("Enter an ID Number: ")

    if id_num in employee_dct:

        #Get a new employee name
        name = input("Enter a new employee name: ")

        #Get a new employee department
        department = input("Enter a new employee department: ")

        #Get a new employee job title
        job_title = input("Enter a new employee job title: ")

        #Create a contact object named entry
        worker = employee.Employee(name, id_num, department, job_title)

        #Update the entry
        employee_dct[id_num] = worker
        print("Information updated.")
    else:
        print("That ID Number is not found.")



#Function to delete an entry from the specified dictionary
def delete(employee_dct):

    #Prompt for ID number to look up
    id_num = input("Enter an ID Number: ")

    #If the id_num is found, delete entry 
    if id_num in employee_dct:
        del employee_dct[id_num]
        print("Entry deleted")
    else:
        print("That ID Number is not found.")



#Function to pickle the specified object and saves it to the contact file
def save_employees(employee_dct):
    #Open the file for writing.
    output_file = open(FILENAME, "wb")

    #Pickle the dictionary and save it
    pickle.dump(employee_dct, output_file)

    #Closes the file
    output_file.close()
        


main()
