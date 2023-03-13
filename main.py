class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_l(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.finished_courses and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_grade(self):
        if len(self.grades) > 0:
            aver = 0
            for value in self.grades.values():
                aver += sum(value) / len(value)
            a_grade = aver / len(self.grades)
        else:
            a_grade = "нет оценок"
        return a_grade

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашнее задание: {self.average_grade()}\nКурсы в процессе изучения: {",".join(self.courses_in_progress)}\nЗавершенные курсы: {",".join(self.finished_courses)}'

    def compare(self, opponent):
        if isinstance(opponent, Student):
            if self.average_grade() > opponent.average_grade():
                result = f"Средняя оценка {self.name} {self.surname} выше чем средняя оценка {opponent.name} {opponent.surname}"
            elif self.average_grade() < opponent.average_grade():
                result = f"Средняя оценка {self.name} {self.surname} ниже чем средняя оценка {opponent.name} {opponent.surname}"
            else:
                result = "Оценки одинаковые"
            print(result)
        else:
            print("ошибка")

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []
        self.grades = {}

    def average_grade(self):
        if len(self.grades) > 0:
            aver = 0
            for value in self.grades.values():
                aver += sum(value) / len(value)
            a_grade = aver / len(self.grades)
        else:
            a_grade = "нет оценок"
        return a_grade

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_grade()}'

    def compare(self, opponent):
        if isinstance(opponent, Lecturer):
            if self.average_grade() > opponent.average_grade():
                result = f"Средняя оценка {self.name} {self.surname} выше чем средняя оценка {opponent.name} {opponent.surname}"
            elif self.average_grade() < opponent.average_grade():
                result = f"Средняя оценка {self.name} {self.surname} ниже чем средняя оценка {opponent.name} {opponent.surname}"
            else:
                result = "Оценки одинаковые"
            print(result)
        else:
            print("ошибка")


class Reviewer(Mentor):
    def __int__(self, name, surname):
        super().__int__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.finished_courses:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'

def aver_grade_students(student_list, course):
    all_grade = 0
    i = 0
    for student in student_list:
        if isinstance(student, Student) and course in student.finished_courses:
            all_grade += sum(student.grades.get(course))/len(student.grades.get(course))
            i += 1
        else:
            continue
    if i > 0:
        a_grade = all_grade/i
    else:
        a_grade = 'Не верные данные'
    return f'Средняя оценка по курсу {course}: {a_grade}'

def aver_grade_lecturers(lecturer_list, course):
    all_grade = 0
    i = 0
    for lecturer in lecturer_list:
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached:
            all_grade += sum(lecturer.grades.get(course))/len(lecturer.grades.get(course))
            i += 1
        else:
            continue
    if i > 0:
        a_grade = all_grade/i
    else:
        a_grade = 'Не верные данные'
    return f'Средняя оценка за лекции по курсу {course}: {a_grade}'



student_1 = Student('Megan', 'Fox', 'your_gender')
student_1.finished_courses += ['Python']
student_1.finished_courses += ['Git']
student_1.courses_in_progress += ['Работа с API']

student_2 = Student('Tom', 'Hanks', 'your_gender')
student_2.finished_courses += ['Git']
student_2.finished_courses += ['Python']

lecturer1 = Lecturer('Will', 'Smith')
lecturer1.courses_attached += ['Python']
lecturer1.courses_attached += ['Git']

lecturer2 = Lecturer('Edward', 'Norton')
lecturer2.courses_attached += ['Python']
lecturer2.courses_attached += ['Git']

reviewer1 = Reviewer('Brad', 'Pitt')
reviewer1.courses_attached += ['Python']
reviewer1.courses_attached += ['Git']

reviewer2 = Reviewer('Tom', 'Cruise')
reviewer2.courses_attached += ['Python']
reviewer2.courses_attached += ['Git']

reviewer1.rate_hw(student_1, 'Python', 9)
reviewer1.rate_hw(student_1, 'Git', 5)
reviewer1.rate_hw(student_2, 'Python', 10)
reviewer1.rate_hw(student_2, 'Git', 8)

reviewer2.rate_hw(student_1, 'Python', 6)
reviewer2.rate_hw(student_1, 'Git', 8)
reviewer2.rate_hw(student_2, 'Python', 9)
reviewer2.rate_hw(student_2, 'Git', 10)

student_1.rate_l(lecturer1, 'Python', 10)
student_1.rate_l(lecturer1, 'Git', 8)
student_2.rate_l(lecturer1, 'Python', 5)
student_2.rate_l(lecturer1, 'Git', 7)

student_1.rate_l(lecturer2, 'Python', 10)
student_1.rate_l(lecturer2, 'Git', 7)
student_2.rate_l(lecturer2, 'Python', 5)
student_2.rate_l(lecturer2, 'Git', 7)

print(reviewer1)
print(lecturer1)
print(student_1)


lecturer2.compare(lecturer1)
student_1.compare(student_2)

print(aver_grade_students([student_1, student_2], 'Api'))
print(aver_grade_lecturers([lecturer1, lecturer2], 'Python'))
