class Employee:
    # 1. Class-level data: shared by all instances and the class itself
    company = "OpenAI"

    # 2. Class Method: takes the class (cls) as its first argument
    @classmethod
    def change_company(cls, new_name):
        # Successfully changes the class variable
        cls.company = new_name

    # 3. Static Method: takes no mandatory arguments (like cls or self)
    @staticmethod
    def try_change_company(new_name):
        # This creates a NEW LOCAL variable named 'company',
        # it does NOT change the class variable Employee.company
        company = new_name

# Call both methods directly on the class
Employee.change_company("Google")
print("After classmethod:", Employee.company)

Employee.try_change_company("Meta")
print("After staticmethod:", Employee.company)