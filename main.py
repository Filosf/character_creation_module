from random import randint


def attack(char_name, char_class):
    if char_class == 'warrior':
        n = 5 + randint(3, 5)
        return (f'{char_name} нанёс урон противнику равный {n}')
    if char_class == 'mage':
        n = 5 + randint(5, 10)
        return (f'{char_name} нанёс урон противнику равный {n}')
    if char_class == 'healer':
        n = 5 + randint(-3, -1)
        return (f'{char_name} нанёс урон противнику равный {n}')
    return (f'{char_name} не нанес урона противнику')


def defence(char_name, char_class):
    if char_class == 'warrior':
        n = 10 + randint(5, 10)
        return (f'{char_name} блокировал {n} урона')
    if char_class == 'mage':
        n = 10 + randint(-2, 2)
        return (f'{char_name} блокировал {n} урона')
    if char_class == 'healer':
        n = 10 + randint(2, 5)
        return (f'{char_name} блокировал {n} урона')
    return (f'{char_name} не блокироваел урон')


def special(char_name, char_class):
    if char_class == 'warrior':
        n = 105
        return (f'{char_name} применил специальное умение «Выносливость {n}»')
    if char_class == 'mage':
        return (f'{char_name} применил специальное умение «Атака {45}»')
    if char_class == 'healer':
        return (f'{char_name} применил специальное умение «Защита {40}»')
    return (f'{char_name} не применил специальное умение')


def start_training(char_name, char_class):
    if char_class == 'warrior':
        print(f'{char_name}, ты Воитель — отличный боец ближнего боя.')
    if char_class == 'mage':
        print(f'{char_name}, ты Маг — превосходный укротитель стихий.')
    if char_class == 'healer':
        print(f'{char_name}, ты Лекарь — чародей, способный исцелять раны.')
    print('Потренируйся управлять своими навыками.')
    print('Введи одну из команд: attack — чтобы атаковать', end='')
    print(' противника, defence — чтобы блокировать атаку противника', end='')
    print('или special — чтобы использовать свою суперсилу.')
    print('Если не хочешь тренироваться, введи команду skip.')
    cmd = None
    while cmd != 'skip':
        cmd = input('Введи команду: ')
        if cmd == 'attack':
            print(attack(char_name, char_class))
        if cmd == 'defence':
            print(defence(char_name, char_class))
        if cmd == 'special':
            print(special(char_name, char_class))
    return 'Тренировка окончена.'


def choice_char_class():
    approve_choice = None
    char_class = None
    while approve_choice != 'y':
        print('Введи название персонажа, за которого хочешь играть:', end=' ')
        char_class = input('Воитель — warrior, Маг — mage, Лекарь — healer: ')
        if char_class == 'warrior':
            print('Воитель — дерзкий воин ближнего боя.', end=' ')
            print('Сильный, выносливый и отважный.')
        if char_class == 'mage':
            print('Маг — находчивый воин дальнего боя.', end=' ')
            print('Обладает высоким интеллектом.')
        if char_class == 'healer':
            print('Лекарь — могущественный заклинатель.', end=' ')
            print('Черпает силы из природы, веры и духов.')
        print('Нажми (Y), чтобы подтвердить выбор,', end=' ')
        print('или любую другую кнопку,', end=' ')
        approve_choice = input('чтобы выбрать другого персонажа ').lower()
    return char_class


def main():
    print('Приветствую тебя, искатель приключений!')
    print('Прежде чем начать игру...')
    char_name = input('...назови себя: ')
    print(f'Здравствуй, {char_name}! '
          'Сейчас твоя выносливость — 80, атака — 5 и защита — 10.')
    print('Ты можешь выбрать один из трёх путей силы:')
    print('Воитель, Маг, Лекарь')
    char_class = choice_char_class()
    print(start_training(char_name, char_class))


main()
