from oop import Student, Group
import pytest

# Проверка на возраст
def test_wrong_kurs():
    with pytest.raises(ValueError):
        stud_1 = Student(1, 'Кагарманов Родион Радикович', 'м', 10, '890478747976', 'test@test,ru', 2,
                         {"отлично": 5, "хорошо": 3, "удовлетворительно": 2, "неудовлетворительно": 0})
# Проверка на студбилеит
def test_wrong_studbilet():
    with pytest.raises(TypeError):
        stud_1 = Student("1", 'Кагарманов Родион Радикович', 'м', 18, '890478747976', 'test@test,ru', 2,
                         {"отлично": 5, "хорошо": 3, "удовлетворительно": 2, "неудовлетворительно": 0})

# Проверяем увеличение курса
def test_increase_kurs():
    stud_1 = Student(1, 'Кагарманов Родион Радикович', 'м', 18, '890478747976', 'test@test,ru', 2,
                     {"отлично": 5, "хорошо": 3, "удовлетворительно": 2, "неудовлетворительно": 0})

    stud_1.increase_kurs()
    assert stud_1.kurs == 3

# Сравниваем двух студентов по курсу
def test_students_lt():
    stud_1 = Student(1, 'Кагарманов Родион Радикович', 'м', 18, '890478747976', 'test@test,ru', 2,
                     {"отлично": 5, "хорошо": 3, "удовлетворительно": 2, "неудовлетворительно": 0})

    stud_2 = Student(1, 'Тестов Тест Тест', 'м', 18, '890478747976', 'test@test,ru', 1,
                     {"отлично": 5, "хорошо": 3, "удовлетворительно": 2, "неудовлетворительно": 0})

    assert (stud_1 < stud_2) == False

# Проверка при добавлении студента в группу. (неверный тип)
def test_wrong_type_Group():
    with pytest.raises(TypeError):
        group_1 = Group("ИС", 195, "Смирнов И.В.")
        group_1.append("Петров А.Н.")

# Проверка при добавлении сотрудника в отдел (добавтли правильно)
def test_append_Group():
    with pytest.raises(TypeError):
        stud_1 = Student(1, 'Кагарманов Родион Радикович', 'м', 18, '890478747976', 'test@test,ru', 2,
                         {"отлично": 5, "хорошо": 3, "удовлетворительно": 2, "неудовлетворительно": 0})
        group_1 = Group("ИС", 195, "Смирнов И.В.")
        count_before = len(group_1.students)
        group_1.append(group_1)
        assert count_before == len(group_1.students) - 1