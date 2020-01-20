# Define a Python class named Student. This class will have 5 properties.

# First name (string)
# Last name (string)
# Age (integer)
# Cohort number (integer)
# Full name (read-only string)

class Student():
    def __init__(self, first_name, last_name):
        self.__first_name = first_name
        self.__last_name = last_name

    # Define getters for all properties.
    @property
    def first_name(self):
        try: 
            return self.__first_name
        except AttributeError:
            return "none"

    @property
    def last_name(self):
        try:
            return self.__last_name
        except AttributeError:
            return "none"

    @property
    def age(self):
        try:
            return self.__age
        except AttributeError:
            return 0

    @property 
    def cohort_number(self):
        try:
            return self.__cohort_number
        except AttributeError:
            return 0

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"


    # Define a setter for all but the read only property.
    @first_name.setter
    def first_name(self, name):
        if type(name) is str:
            self.__first_name = name
        else:
            raise TypeError('Name must be a string.')

    @last_name.setter
    def last_name(self, name):
        if type(name) is str:
            self.__last_name = name
        else:
            raise TypeError('Name must be a string.')

    @age.setter
    def age(self, number):
        if type(number) is int:
            self.__age = number
        else:
            raise TypeError('Age must be an integer')

    @cohort_number.setter
    def cohort_number(self, number):
        if type(number) is int:
            self.__cohort_number = number
        else:
            raise TypeError('Cohort number must be an integer')

    def __str__(self):
        try:
            return f"{self.full_name} is {self.age} years old and is in cohort {self.__cohort_number}."
        except AttributeError:
            return "Student must be assigned a cohort number."


ryan = Student("Ryan", "Crowley")

ryan.age = 33
ryan.cohort_number = 36
print(ryan)
    



