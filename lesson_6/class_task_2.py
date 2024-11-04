class Person:
    def __init__(self, name):
        self._name=name

    def get_name(self):
        return self._name


class Student(Person):
    def __init__(self,name,student_id):
        super().__init__(name)
        self.__student_id=student_id

    def display_student_id(self):
        return self.__student_id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,new_name):
        self._name=new_name

    @property
    def student_id(self):
        return self.__student_id

person=Person("Michal")
print(person.get_name())

student=Student("Yoni","87654")
print(student.name)
print(student.display_student_id())

student.name="Roni"
print(student.name)