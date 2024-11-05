from xml.etree.ElementPath import prepare_parent


class Person:
    def __init__(self,name):
        self.name=name

    def get_name(self):
        return self.name

class Employee(Person):
    def __init__(self, name,salary, role):
        super().__init__(name)
        self.__salary=salary
        self.__role=role

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self,value:float):
        try:
            if(value<=0):
                raise ValueError("salary must be positive.")
            self.__salary = value
        except ValueError as e:
            print(f"error: {e}")

    @property
    def role(self):
        return self.__role

    @role.setter
    def role(self,value: str):
        try:
            if(len(value)==0):
                 raise ValueError("The role value cannot be empty.")
            self.__role=value
        except ValueError as e:
            print(f"error: {e}")

employee=Employee("Rachel",5000,"teacher")
print(employee.get_name())
print(employee.salary)
print(employee.role)
employee.salary=-8000
employee.role=""
