class Person:
    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name

    def get_full_name(self) -> str:
        print("get full name called")
        return f'{self.first_name} {self.last_name}'

    def perform_action(self):
        print("perform action called")

class Student(Person):
    def __init__(self, first_name, last_name, grade):
        self.grade = grade
        super().__init__(first_name, last_name)

    def get_full_name(self):
        x = super().get_full_name()
        return f'{x}, {self.grade}'

    def perform_action(self):
        print("student perform action called")

def main():
    person = Person("Jayantha", "Senawiratne")
    student = Student("Sayumee", "senawiratne", "A")
    person.get_full_name()
    person.perform_action()
    student.get_full_name()
    student.perform_action()
if __name__ == '__main__':
    main()




