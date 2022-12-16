class Bird:
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def describe(self, full=False):
        return f'Размер птицы {self.name} — {self.size}.'


class Parrot(Bird):
    def __init__(self, name, size, color):
        super().__init__(name, size)
        self.color = color

    def describe(self, full=False):
        if full:
            return (f'Размер пингвина name из рода genus — size.'
                    'Интересный факт: однажды группа геологов-разведчиков '
                    'похитила пингвинье яйцо, и их принялась преследовать '
                    'вся стая, не пытаясь, впрочем, при этом нападать. '
                    'Посовещавшись, похитители вернули птицам яйцо, и те отстали.')
        else:
            super().describe()


class Penguin(Bird):
    def __init__(self, name, size, genus):
        super().__init__(name, size)
        self.genus = genus
    
    def describe(self, full=False):
        if full:
            return (f'Размер пингвина {self.name} из рода {self.genus} — {self.size}.'
                    'Интересный факт: однажды группа геологов-разведчиков '
                    'похитила пингвинье яйцо, и их принялась преследовать '
                    'вся стая, не пытаясь, впрочем, при этом нападать. '
                    'Посовещавшись, похитители вернули птицам яйцо, и те отстали.')
        else:
            super().describe()


kesha = Parrot('Ара', 'средний', 'красный')
kowalski = Penguin('Королевский', 'большой', 'Aptenodytes')

# Вызов метода у созданных объектов.
print(kesha.describe())
print(kowalski.describe(True))