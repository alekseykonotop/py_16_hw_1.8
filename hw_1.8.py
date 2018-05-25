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
    location = 'ferme'
    housing = None  # для разных типов животных разные корпуса
    animal_count = 0  # Общее колличество животных на ферме
    