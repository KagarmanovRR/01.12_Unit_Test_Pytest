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