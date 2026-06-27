# ------------------------------------------------------------------------------------------ #
# Title: Assignment07
# Desc: This assignment demonstrates using data classes with structured error handling
# New concepts: adds set of data classes
# Change Log: (Who, When, What)
#   thcov,6/17/2026,Created Script from starter copy
#   thcov,6/17/2026,Added Student class
#   thcov,6/17/2026,Added my docstrings from Assign.06
#   thcov,6/25/2026,Reformmated docstrings
#   thcov,6/26/2026,Removed commented-out code (saved a copy with commented-out code in archive)
# ------------------------------------------------------------------------------------------ #
import json

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
FILE_NAME: str = "Enrollments.json"

# Define the Data Variables
students: list = [] # table of student data
menu_choice: str  # Holds the choice made by the user.

# Person Class
class Person:
    """A class representing person data.
    Properties:
    - first_name (str): The student's first name.
    - last_name (str): The student's last name.

    ChangeLog:
    thcov,6/19/2026,Created the class
    thcov,6/19/2026,Added __init__
    thcov,6/22/2026,Added __str__
    thcov,6/22/2026,Added getters and setters for first_name and last_name"""

    def __init__(self, first_name: str = '', last_name: str = ''):
        """Initialize a Person instance.
        Args:
        - first_name (str): The student's first name.
        - last_name (str): The student's last name.

        ChangeLog: (Who, When, What)
        thcov,6/22/2026,Created the function"""
        # Adds first_name and last_name properties to the constructor
        self.first_name = first_name
        self.last_name = last_name

    # Getter and setter for the first_name property
    @property # Getter/accessor
    def first_name(self):
        return self.__first_name.title() # Formatting code

    @first_name.setter # Setter
    def first_name(self, value:str):
        if value.isalpha() or value == "": # is character or empty string
            self.__first_name = value
        else:
            raise ValueError("The first name is restricted to alphabetic characters only.")

    # Getter and setter for the last_name property
    @property # Getter/accessor
    def last_name(self):
        return self.__last_name.title() # Formatting code

    @last_name.setter # Setter
    def last_name(self, value: str):
        if value.isalpha() or value == "": # Is character or empty string
            self.__last_name = value
        else:
            raise ValueError("The last name is restricted to alphabetic characters only.")

    # Overrides the __str__() method to return Person data
    def __str__(self):
        """Return a human-readable string representation of the Person.
        This method is called by 'str(obj)' and 'print(obj)'.

        ChangeLog: (Who, When, What)
        thcov,6/22/2026,Created function

        :return: message displaying Firstname, Lastname.
        :rtype: string"""
        return f"{self.first_name},{self.last_name}"

# Student class inherits from the Person class
class Student(Person):
    """This class represents student data
    Properties:
    - first_name: str: Student's first name.
    - last_name: str: Student's last name.
    - course_name: str: Name of course.

    ChangeLog: (Who, When, What)
    thcov,6/17/2026,Created class
    thcov,6/19/2026,Added __init__
    thcov,6/22/2026,Added getter and setter for course name
    thcov,6/22/2026 Added __str__"""

    def __init__(self, first_name: str = '', last_name: str = '',
                 course_name: str = ''):
        """Constructor method that initializes a new Student object with
        first name and last name (both inherited through the Person class)
        and course name (from this class).

        ChangeLog: (Who, When, What)
        thcov, 6/19/2026,Created initializer"""
        # Calls to the Person constructor and passes first_name and last_name data
        super().__init__(first_name=first_name, last_name=last_name)
        # Assigns course_name property to the course_name parameter
        self.course_name= course_name

    # Getter for course_name
    @property # Getter/accessor
    def course_name(self):
        return self.__course_name

    # Setter for course_name
    @course_name.setter # Setter
    def course_name(self, value: str):
        self.__course_name = value

    # Overrides the __str__() method to return the Student data
    def __str__(self):
        """Return a concise, user-friendly description of Student.

        ChangeLog: (Who, When, What)
        thcov,6/22/2026,Created function

        :return: A message displaying Firstname, Lastname, Course
        :rtype: string"""
        return f'{self.first_name},{self.last_name},{self.course_name}'

# Processing --------------------------------------- #
class FileProcessor:
    """A collection of processing layer functions that work
    with processing JSON files

    ChangeLog: (Who, When, What)
    thcov,6/17/2026,Created class
    thcov,6/17/2026,Added function: write_data_to_file
    thcov,6/17/2026,Added function: read_data_from_file"""

    @staticmethod
    def read_data_from_file(file_name: str, student_data: list):
        """This function reads from file with json.load(), returning list[dict]; loop
        converts each dict → Student() object, returns list of Student objects.

        ChangeLog: (Who, When, What)
        thcov,6/17/2026,Created function
        thcov,6/17/2026,Renamed 'json_students' → 'list_of_dict_data'
        thcov,6/17/2026,Converted list of dict rows → list of Student objects via loop
        thcov,6/19/2026,Added student_data: list as a 2nd param

        :param file_name: JSON file we are loading into the script
        :type file_name: string
        :param student_data: to be loaded with the file data
        :type student_data: list of Student objects
        :return: list of Student objects loaded from JSON file
        :rtype: list of Student objects"""
        file = None

        try:
            file = open(file_name, "r")
            list_of_dict_data: list[dict] = json.load(file) # Returns list of dict rows from file
            for row in list_of_dict_data: # Converts list of dict rows into Student objects
                student_object: Student = Student(first_name= row["FirstName"],
                                              last_name= row["LastName"],
                                              course_name= row["CourseName"])
                student_data.append(student_object)
        except Exception as e:
            IO.output_error_messages(message="Error: There was a problem with reading the file.", error=e)
        finally:
            if file is not None and not file.closed:
                file.close()
        return student_data

    @staticmethod
    def write_data_to_file(file_name: str, student_data: list):
        """This function saves student data to a JSON file: Converts data
        from list of Student objs → list of dict rows and writes to JSON file via json.dump().

        ChangeLog: (Who, When, What)
        thcov,6/17/2026,Created function
        thcov,6/17/2026,Renamed 'students_json' → 'list_of_dict_data'
        thcov,6/19/2026,Defined list_of_dict_data
        thcov,6/19/2026,Converted list of Student objects → list[dict] via loop
        thcov,6/26/2026,Removed call to output_student_and_course_names

        :param file_name: JSON file the data will be saved to
        :type file_name: string
        :param student_data: data to be loaded into file
        :type student_data: list of Student objects
        :return: None"""
        file = None

        try:
            list_of_dict_data: list = [] # to hold json data to use with the json.dump() function
            for student in student_data: # Converts list of Student objects to list of dict rows
                student_dict: dict = {"FirstName": student.first_name,
                                      "LastName": student.last_name,
                                      "CourseName": student.course_name}
                list_of_dict_data.append(student_dict)

            file = open(file_name, "w")
            json.dump(list_of_dict_data, file, indent=2)
        except Exception as e:
            message = "Error: There was a problem with writing to the file.\n"
            message += "Please check that the file is not open by another program."
            IO.output_error_messages(message=message,error=e)
        finally:
            if file is not None and file.closed == False:
                file.close()


# Presentation --------------------------------------- #
class IO:
    """A collection of presentation layer functions that manage user input and output

    ChangeLog: (Who, When, What)
    thcov,6/17/2026,Created Class
    thcov,6/17/2026,Added output_error_messages
    thcov,6/17/2026,Added output_menu
    thcov,6/17/2026,Added input_menu_choice
    thcov,6/17/2026,Added output_student_and_course_names
    thcov,6/17/2026,Added input_student_data"""

    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        """This function outputs custom error messages to the user

        ChangeLog: (Who, When, What)
        thcov,6/17/2026,Created function

        :param message: custom error message to display (string)
        :param error: Exception with technical information to display to user
        :return: None"""
        print(message, end="\n\n")
        if error is not None:
            print("-- Technical Error Message -- ")
            print(error, error.__doc__, type(error), sep='\n')

    @staticmethod
    def output_menu(menu: str):
        """This function displays the Course Registration Program
        menu to the user

        ChangeLog: (Who, When, What)
        thcov,6/17/2026,Created function

        :param menu: the string of the Course Registration Program menu
        :type menu: string
        :return: None"""
        print()  # Adding extra space to make it look nicer.
        print(menu)
        print()  # Adding extra space to make it look nicer.

    @staticmethod
    def input_menu_choice():
        """This function gets a menu selection from the user: "1", "2", "3", or "4"

        ChangeLog: (Who, When, What)
        thcov,6/17/2026,Created function

        :return: user's menu selection
        :rtype: str"""
        choice = "0"
        while True:
            try:
                choice = input("Enter your menu choice number: ")
                if choice not in ("1","2","3","4"):  # Note these are strings
                    raise Exception("Please choose only 1, 2, 3, or 4.")
                return choice
            except Exception as e:
                IO.output_error_messages(e.__str__())  # Not passing e to avoid the technical message

    @staticmethod
    def output_student_and_course_names(student_data: list):
        """This function displays to the user a string of comma-separated values
        for each row in student_data

        ChangeLog: (Who, When, What)
        thcov,6/17/2026,Created function
        thcov,6/20/2026,Added code to access Student obj. instead of dict. data

        :param student_data: the student enrollment data to display to user (list of dict rows)
        :type student_data: list of Student objects
        :return: None"""
        print("-" * 50)
        # Accesses Student object data (instead of dict. data)
        for student in student_data:
            print(f'{student.first_name},{student.last_name},{student.course_name}')
        print("-" * 50)

    @staticmethod
    def input_student_data(student_data: list):
        """This function gets the student's first name, last name, and course name
        from the user and appends it to student_data

        ChangeLog: (Who, When, What)
        thcov,6/17/2026,Created function
        thcov,6/20/2026,Updated code to create new student instead of adding to dict.
        thcov,6/20/2026,Commented out the existing input and validation code
        thcov,6/22/2026,Added code to create a new student object using each property's
        validation code

        :param student_data: contains current data; to be appended to with the user input data
        :type student_data: list of Student objects
        :return: list of data including the new input data
        :rtype: list of Student objects"""
        try:
            student = Student() # Note: this will use the default empty string arguments
            student.first_name = input("Please enter the student's first name: ")
            student.last_name = input("Please enter the student's last name: ")
            student.course_name = input("Please enter the name of the course: ")
            student_data.append(student) # This adds a Student object to the list
            print(f"You have registered {student.first_name} {student.last_name} for {student.course_name}.")
        except ValueError as e:
            IO.output_error_messages(message="Error: One or more values entered were the incorrect data type.", error=e)
        except Exception as e:
            IO.output_error_messages(message="Error: There was a problem with the data you entered.", error=e)
        return student_data

# End of function definitions

# Beginning of main body of the script
# When the program starts, read the file data into a list of lists (table)
# Extract the data from the file
students = FileProcessor.read_data_from_file(file_name=FILE_NAME, student_data=students)

# Present and Process the data
while True:

    # Present the menu of choices
    IO.output_menu(menu=MENU)
    menu_choice = IO.input_menu_choice()

    # Input user data
    if menu_choice == "1":  # This will not work if it is an integer!
        students = IO.input_student_data(student_data=students)
        continue

    # Present the current data
    elif menu_choice == "2":
        IO.output_student_and_course_names(student_data=students)
        continue

    # Save the data to a file
    elif menu_choice == "3":
        FileProcessor.write_data_to_file(file_name=FILE_NAME, student_data=students)
        continue

    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop

print("Program Ended")
