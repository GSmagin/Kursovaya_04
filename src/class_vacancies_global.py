import json
import re


class VacanciesGlobal:
    """docstring for VacanciesHH"""

    def __init__(self, class_copy):
        # with open(filename, 'r', encoding='utf-8') as file:
        self.class_copy = [].append(class_copy)

    def __len__(self):
        return len(self.class_copy)

    def __repr__(self):
        return str(self.class_copy)

    def __add__(self, other):
        return self.class_copy.append(other)

    def __str__(self):
        return self.class_copy