class Student:
    marks = []
    #ФИО, пол, возраст, телефон, почта, курс, оценки
    def __init__(self, number, fio, gender, age, tel, email, kurs, marks):
        if type(number) != int:
            raise TypeError("Номер студента должен быть числовым")
        self.number = int(number)
        self.fio = fio
        self.gender = gender
        if age < 14:
            raise ValueError("До получения паспорта неьзя поступить в техникум")
        self.age = int(age)
        self.tel = tel
        self.email = email
        self.kurs = int(kurs)
        self.marks = marks
        #for key, val in marks.items():
        #   print(key, '-', val)

    # Метод добавления оценок для студента.

    # Метод перевода студента на курс выше.
    def increase_kurs(self):
        self.kurs += 1

    # Перехват функции print, когда она преобразует свое значение в строку
    def __str__(self):
        return f"{'Студент' if self.gender=='м' else 'Студентка'}: {self.fio}" \
               f" на {self.kurs} курсе, номер студ.билета: {self.number}"

    # Предусмотреть операции сравнения студентов по курсу.
    def __lt__(self, other):
        return self.kurs < other.kurs
    def __le__(self, other):
        return self.kurs <= other.kurs
    def __eq__(self, other):
        return self.kurs == other.kurs

class Group:
    #Группы – содержат студентов; Атрибуты: название, номер.
    def __init__(self, title, nomer, students=None):
        self.title = title
        self.nomer = int(nomer)
        if students is None:
            students = list()
        self.students = students

    # Добавляем студента в группу
    def append(self, stud):
        self.students.append(stud)

    def __str__(self):
        return f"Группа: {self.nomer}{self.title}, Количество сотрудников: {len(self.students)}"

    # вывод всех студентов группы.
    def print_students(self):
        for stud in self.students:
            print(stud)

    # Вывод всех мальчиков/ девочек группы.
    def print_boys(self):
        for stud in self.students:
            if stud.gender == "м":
                print(stud)

    def print_girls(self):
        for stud in self.students:
            if stud.gender == "ж":
                print(stud)

    # Предусмотреть операции сравнения по количеству студентов в группе.
    def __lt__(self, other):
        return len(self.students) < len(other.students)
    def __le__(self, other):
        return len(self.students) <= len(other.students)
    def __eq__(self, other):
        return len(self.students) == len(other.students)


