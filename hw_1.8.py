# coding=utf-8
# Домашнее задание к лекции 1.7 «Классы и их применение в Python»
# Необходимо реализовать классы животных на ферме:
#       Коровы, козы, овцы, свиньи;
#       Утки, куры, гуси.
#       Условия:
#
# Должен быть один базовый класс, который наследуют все остальные животные.
# Базовый класс должен определять общие характеристики и интерфейс.


class FarmAnimals():
    location = 'Животноводческое хозяйство Зайцево.'
    animal_count = 0

    def __init__(self, name, an_type=None, food=None):
        self.name = name
        self.an_type = an_type
        self.food = food
        FarmAnimals.animal_count += 1
        print('На ферме появилось новое животное по кличке {0}, тип {1}.'.format(self.name, self.an_type))

    @staticmethod
    def report():
        """Метод выводит отчет о численности животных на ферме."""

        if FarmAnimals.animal_count == 0:
            print('Животных нет.')
        elif FarmAnimals.animal_count == 1:
            print('Есть 1 животное')
        else:
            print('Всего {0} животных'.format(FarmAnimals.animal_count))

    def what_food(self):
        print('{0} - это {1}, нужен корм: {2}.'.format(self.name, self.an_type, self.food))


class Cow(FarmAnimals):
    an_type = 'корова'
    food = 'грубые корма, сочные корма, зеленые корма'

    def __init__(self, name):
        super(Cow, self).__init__(name, Cow.an_type, Cow.food)


class Goat(FarmAnimals):
    an_type = 'коза'
    food = 'сочные корма, зеленые корма'

    def __init__(self, name):
        super(Goat, self).__init__(name, Goat.an_type, Goat.food)


class Sheep(FarmAnimals):
    an_type = 'овца'
    food = 'сочные корма, зеленые корма'

    def __init__(self, name):
        super(Sheep, self).__init__(name, Sheep.an_type, Sheep.food)


class Pig(FarmAnimals):
    an_type = 'свинья'
    food = 'рожь, пшеница, тыква, сахарная свекла, горох, просо, комбинированный силос, отходы молочного производства'

    def __init__(self, name):
        super(Pig, self).__init__(name, Pig.an_type, Pig.food)


class Duck(FarmAnimals):
    an_type = 'утка'
    food = 'мука зерновая, мука костная, отруби, морковь, свекла, проросшее зерно, вареный картофель, тыква'

    def __init__(self, name):
        super(Duck, self).__init__(name, Duck.an_type, Duck.food)


class Chicken(FarmAnimals):
    an_type = 'курица'
    food = 'комбикорм'

    def __init__(self, name):
        super(Chicken, self).__init__(name, Chicken.an_type, Chicken.food)


class Goose(FarmAnimals):
    an_type = 'гусь'
    food = 'силос, сенная мука, морковь, свекла, пшеничные отруби, мел, ракушка, овес, ячмень'

    def __init__(self, name):
        super(Goose, self).__init__(name, Goose.an_type, Goose.food)


cow = Cow('Буренка')
goat = Goat('Снежка')
sheep = Sheep('Хавроша')
pig = Pig('Борька')
duck = Duck('Кряква')
chicken = Chicken('Бьянка')
goose = Goose('Вега')

FarmAnimals.report()

print(cow.an_type)
cow.what_food()

print(goat.an_type)
goat.what_food()

print(duck.an_type)
duck.what_food()

print(goose.an_type)
goose.what_food()




# ============ Не верное решение ============


# class FarmAnimals:
#     location = 'Ферма'
#     # housing = None  # для разных типов животных разные корпуса
#     animal_count = 0  # Общее колличество животных на ферме
#
#     def __init__(self, name, obj_type):
#         self.name = name
#         self.obj_type = obj_type
#         FarmAnimals.animal_count += 1
#
#     def present_new_animal(self):
#         """Метод сообщает о новом представителе класса."""
#         print('Новое животное на ферме: тип {0}, кличкa {1}'.format(self.obj_type, self.name))
#
#     @staticmethod
#     def report():
#         """Метод выводит отчет о численности животных на ферме."""
#         print('Всего животных на ферме: ', FarmAnimals.animal_count)
#
#
# # Класс Прупные животные к которым относятся коровы, козы, овца, свиньи
# class LargeAnimals(FarmAnimals):
#     housing = '"КРС"'  # Корпус крупного рогатого скота
#     count_in_housing = 0
#
#     def __init__(self, name, obj_type):
#         FarmAnimals.__init__(self, name, obj_type)
#         FarmAnimals.present_new_animal(self)
#         LargeAnimals.count_in_housing += 1
#
#     @staticmethod
#     def how_many():
#         """Выводит общее кол-во представителей класса LargeAnimals."""
#         print('В корпусе {0} всего {1} животных'.format(LargeAnimals.housing, LargeAnimals.count_in_housing))
#
#
# class Cow(LargeAnimals):
#
#
#     def __ini__(self, name, obj_type):
#         super(Cow, name, obj_type)
#
# cow33 = Cow('Новая Буренка', 'корова')
#
#
# # Класс Пернатые, в которым относятся куры, гуси, утки
# class FeatheryAnimals(FarmAnimals):
#     housing = '"Пернатые"'  # Корпус пернатых животных
#     count_in_housing = 0
#
#     def __init__(self, name, obj_type):
#         FarmAnimals.__init__(self, name, obj_type)
#         FarmAnimals.present_new_animal(self)
#         FeatheryAnimals.count_in_housing += 1
#
#     @staticmethod
#     def how_many():
#         """Выводит общее кол-во животных в корпусе"""
#         print('В корпусе {0} всего {1} животных'.format(FeatheryAnimals.housing, FeatheryAnimals.count_in_housing))


# Создадим несколько объектов класса LargeAnimals
# cow1 = LargeAnimals('Буренка', 'корова')
# cow2 = LargeAnimals('Бурая', 'корова')
# goat = LargeAnimals('Снежка', 'коза')
# sheep = LargeAnimals('Хавроша', 'овца')
# pig = LargeAnimals('Борька', 'свинья')
#  Узнаем локацию и в каком именно корпусе проживает животное cow1
# print('Животное по кличке {0} находится на: {1} в корпусе {2}'.format(cow1.name, cow1.location, cow1.housing))

# Узнаем кол-во объектов( животных) класса LargeAnimals
# LargeAnimals.how_many()

# Создадим несколько объектов класса FeatheryAnimals
# duck = FeatheryAnimals('Кряква', 'утка')
# chicken = FeatheryAnimals('Бьянка', 'курица')
# goose = FeatheryAnimals('Вега', 'гусыня')
# Узнаем кол-во объектов( животных) класса LargeAnimals
# FeatheryAnimals.how_many()

#  Узнаем локацию и в каком именно корпусе проживает животное duck
# print('Животное по кличке {0} находится на: {1} в корпусе {2}'.format(duck.name, duck.location, duck.housing))

# Узнаем общее кол-во животных на ферме
# FarmAnimals.report()

