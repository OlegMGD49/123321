import random


class Teacher:
    def __init__(self, th_name, th_age):
        self.th_name = th_name
        self.th_age = th_age

    def __str__(self):
        return f'Учителя зовут: {self.th_name}, и ему {self.th_age} года'

    def teach(self, subject):
        print(f'Преподает {subject.subject_name}')

    def rate(self, student):
        num_1 = random.randint(2, 5)
        print(f"Учитель {self.th_name} ставит оценку студенту {student.student_name} ,{num_1}")
        return num_1


class Student:
    def __init__(self, student_name, student_age, student_Knowledge):
        self.student_name = student_name
        self.student_age = student_age
        self.student_Knowledge = student_Knowledge
        self.rate = None

    def __str__(self):
        return (f'Имя студента: {self.student_name},'
                f' Возраст студента: {self.student_age}, '
                f'Уровень владения предметом: {self.student_Knowledge} ')

    def get_rate(self, teacher):
        self.rate = teacher.rate(self)
        print(f'Студент {self.student_name} узнал оценку: {self.rate}')
        return self.rate

    def go_to_univers(self, subject_1):
        print(f'{self.student_name} ходит на лекции по {subject_1}')


class GoodStudent(Student):
    def __init__(self, student_name, student_age, student_Knowledge):
        super().__init__(student_name, student_age, student_Knowledge)

    def wash_floor(self, teacher):
        if self.rate is None:
            print("Узнаем оценку оценку.")
            return
        if self.rate <= 3:
            print(f'{self.student_name} Моет полы в аудитории для  -> {teacher.th_name} за хорошую оценОЧКУ')
        else:
            print(f'{self.student_name} Очень хорошо трудился, мыть полики для  -> {teacher.th_name} не нужно')


class BadStudent(Student):
    def __init__(self, student_name, student_age, student_Knowledge):
        super().__init__(student_name, student_age, student_Knowledge)

    def give_bribe(self, teacher):
        if self.rate is None:
            print("Узнаем оценку оценку.")
            return
        if self.rate <= 3:
            print(f'{self.student_name} Дает взятку за оценОЧКУ -> {teacher.th_name}')
        else:
            print(f'{self.student_name} Не дает взятку за оценОЧКУ -> {teacher.th_name}')


class Subject:
    def __init__(self, subject_name):
        self.subject_name = subject_name

    def __str__(self):
        return f'{subject_1.subject_name}'


teacher_1 = Teacher('Alex', 44)
subject_1 = Subject('Math')
good_student = GoodStudent('Jon', 23, 23)
bad_student = BadStudent('Muhamed', 33, 23)

bad_student.get_rate(teacher_1)
bad_student.give_bribe(teacher_1)

good_student.go_to_univers(subject_1)
good_student.get_rate(teacher_1)
good_student.wash_floor(teacher_1)
bad_student.go_to_univers(subject_1)
