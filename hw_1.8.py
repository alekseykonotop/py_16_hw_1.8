# coding=utf-8
# Домашнее задание к лекции 1.7 «Классы и их применение в Python»
# Необходимо реализовать классы животных на ферме:
#       Коровы, козы, овцы, свиньи;
#       Утки, куры, гуси.
#       Условия:
#
# Должен быть один базовый класс, который наследуют все остальные животные.
# Базовый класс должен определять общие характеристики и интерфейс.

class FarmAnimals:
    location = 'Ферма'
    # housing = None  # для разных типов животных разные корпуса
    animal_count = 0  # Общее колличество животных на ферме

    def __init__(self, name, type):
        self.name = name
        self.type = type
        FarmAnimals.animal_count += 1

    def present_new_animal(self):
        """Метод сообщает о новом представителе класса."""
        print('Новое животное на ферме: тип {0}, кличкa {1}'.format(self.type, self.name))

    def report():
        """Метод выводит отчет о численности животных на ферме."""
        print('Всего животных на ферме: ', FarmAnimals.animal_count)

# Класс Прупные животные к которым относятся коровы, козы, овца, свиньи
class LargeAnimals(FarmAnimals):
    housing = '"КРС"'  # Корпус крупного рогатого скота
    count_in_housing = 0

    def __init__(self, name, type):
        FarmAnimals.__init__(self, name, type)
        FarmAnimals.present_new_animal(self)
        LargeAnimals.count_in_housing += 1

    def how_many():
        """Выводит общее кол-во представителей класса LargeAnimals."""
        print('В корпусе {0} всего {1} животных'.format(LargeAnimals.housing, LargeAnimals.count_in_housing))


# Класс Пернатые, в которым относятся куры, гуси, утки
class FeatheryAnimals(FarmAnimals):
    housing = '"Пернатые"' # Корпус пернатых животных
    count_in_housing = 0

    def __init__(self, name, type):
        FarmAnimals.__init__(self, name, type)
        FarmAnimals.present_new_animal(self)
        FeatheryAnimals.count_in_housing += 1

    def how_many():
        """Выводит общее кол-во животных в корпусе"""
        print('В корпусе {0} всего {1} животных'.format(FeatheryAnimals.housing, FeatheryAnimals.count_in_housing))


# Создадим несколько объектов класса LargeAnimals
cow1 = LargeAnimals('Буренка', 'корова')
cow2 = LargeAnimals('Бурая', 'корова')
goat = LargeAnimals('Снежка', 'коза')
sheep = LargeAnimals('Хавроша', 'овца')
pig = LargeAnimals('Борька', 'свинья')
#  Узнаем локацию и в каком именно корпусе проживает животное cow1
print('Животное по кличке {0} находится на: {1} в корпусе {2}'.format(cow1.name, cow1.location, cow1.housing))

# Узнаем кол-во объектов( животных) класса LargeAnimals
LargeAnimals.how_many()

# Создадим несколько объектов класса FeatheryAnimals
duck = FeatheryAnimals('Кряква', 'утка')
chicken = FeatheryAnimals('Бьянка', 'курица')
goose = FeatheryAnimals('Вега', 'гусыня')
# Узнаем кол-во объектов( животных) класса LargeAnimals
FeatheryAnimals.how_many()

#  Узнаем локацию и в каком именно корпусе проживает животное duck
print('Животное по кличке {0} находится на: {1} в корпусе {2}'.format(duck.name, duck.location, duck.housing))

# Узнаем общее кол-во животных на ферме
FarmAnimals.report()

