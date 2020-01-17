# Define a Python class named Student. This class will have 5 properties.

# First name (string)
# Last name (string)
# Age (integer)
# Cohort number (integer)
# Full name (read-only string)

class Student():

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

# Ensure that only the appropriate value can be assigned to each.
dan = Student()
print("No first name: ", dan.first_name)
# dan.first_name = 0
dan.first_name = "Dan"
print("First Name: ", dan.first_name)
print()

print("No last name: ", dan.last_name)
# dan.last_name = .2
dan.last_name = "Theman"
print("Last Name: ", dan.last_name)
print()

print("No age: ", dan.age)
# dan.age = "two"
# dan.age = .2
dan.age = 2
print("Age: ", dan.age)
print()

print("No Cohort: ", dan.cohort_number)
# dan.cohort_number = "hi"
# dan.cohort_number = .1
dan.cohort_number = 36
print("Cohort number: ", dan.cohort_number)
print()

# The full name property should return first name and last name separated by a space. It's value cannot be set.
# dan.full_name = "DAN THEMAN"
print("Full Name: ", dan.full_name)