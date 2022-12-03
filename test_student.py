from oop import Student, Group
import pytest

# Проверка на возраст
def test_wrong_kurs():
    with pytest.raises(ValueError):
        stud_1 = Student(1, 'Кагарманов Родион Радикович', 'м', 10, '890478747976', 'test@test,ru', 2,
                         {"отлично": 5, "хорошо": 3, "удовлетворительно": 2, "неудовлетворительно": 0})