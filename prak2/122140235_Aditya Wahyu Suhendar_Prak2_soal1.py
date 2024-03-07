class Student:
    def __init__(self, nim, name, student_class, is_student=True):
        self.__nim = nim
        self.__name = name
        self.__class = student_class
        self.__is_student = is_student

    # Getter and Setter for 'name'
    def get_name(self):
        return self.__name

    def set_name(self, new_name):
        self.__name = new_name

    # Getter and Setter for 'nim'
    def get_nim(self):
        return self.__nim

    def set_nim(self, new_nim):
        self.__nim = new_nim

    def get_student_status(self):
        return self.__is_student

    def enroll(self):
        if self.__is_student:
            return f"{self.__name} has enrolled in {self.__class}."
        else:
            return f"{self.__name} is not a student."

    def submit_assignment(self):
        return f"{self.__name} has submitted an assignment for {self.__class}."

    def take_exam(self):
        return f"{self.__name} is taking an exam for {self.__class}."


# Initiating objects with different values
student1 = Student(nim="001", name="John Doe", student_class="Math")
student2 = Student(nim="002", name="Jane Doe", student_class="Physics", is_student=False)

# Using getter and setter to retrieve and replace values
print(f"Before using setter - Name: {student1.get_name()}, NIM: {student1.get_nim()}")
student1.set_name("John Smith")
student1.set_nim("003")
print(f"After using setter - Name: {student1.get_name()}, NIM: {student1.get_nim()}")

# Performing operations using methods
print(student1.enroll())
print(student1.submit_assignment())
print(student1.take_exam())

print("\n" + "=" * 30 + "\n")

print(f"Before using setter - Name: {student2.get_name()}, NIM: {student2.get_nim()}")
# Trying to use setter without 'is_student' parameter for the second object
# This will raise an error because 'is_student' parameter is not provided
# student2.set_name("Jane Smith")  # Uncommenting this line will raise an error
# student2.set_nim("004")          # Uncommenting this line will raise an error
print(f"After using setter - Name: {student2.get_name()}, NIM: {student2.get_nim()}")

# Performing operations using methods
print(student2.enroll())  # This will raise an error due to missing 'is_student' parameter
