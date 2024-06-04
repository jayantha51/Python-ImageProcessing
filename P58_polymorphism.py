import datetime

class Person:
    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name  = last_name

    def get_full_name(self) -> str:
        print("get full name called")
        return f'{self.first_name} {self.last_name}'

    def perform_action(self):
        print("Person performs action")


class Student(Person):
    def __init__(self, first_name, last_name, grade):
        self.grade = grade
        super().__init__(first_name,last_name)

    def get_full_name(self):
        x = super().get_full_name()
        return f'{x} {self.grade}'


    def perform_action(self):
        print("student performs action")

def main():
    person0 = Person("AB", "CD")
    student0 = Student("EF", "GH", 7)
    print("person.....")
    person0.get_full_name()
    person0.perform_action()

    print("student.....")
    student0.get_full_name()
    student0.perform_action()

if __name__ == '__main__':
    main()
