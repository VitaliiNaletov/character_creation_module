from random import randint

"""Game."""


def attack(char_name, char_class):
    """Атаки."""
    if char_class == 'warrior':
        return (f'{char_name} '
                f'нанёс урон противнику равный {5 + randint(3, 5)}')
    if char_class == 'mage':
        return (f'{char_name} '
                f'нанёс урон противнику равный {5 + randint(5, 10)}')
    if char_class == 'healer':
        return (f'{char_name} '
                f'нанёс урон противнику равный {5 + randint(-3, -1)}')
    return f'{char_name} не нанес удар противнику'


def defence(char_name, char_class):
    """Блокировки ударов."""
    if char_class == 'warrior':
        return f'{char_name} блокировал {10 + randint(5, 10)} урона'
    if char_class == 'mage':
        return f'{char_name} блокировал {10 + randint(-2, 2)} урона'
    if char_class == 'healer':
        return f'{char_name} блокировал {10 + randint(2, 5)} урона'
    return f'{char_name} провал'


def special(char_name, char_class):
    """Использование умений."""
    if char_class == 'warrior':
        return (f'{char_name} '
                f'применил специальное умение «Выносливость {80 + 25}»')
    if char_class == 'mage':
        return f'{char_name} применил специальное умение «Атака {5 + 40}»'
    if char_class == 'healer':
        return f'{char_name} применил специальное умение «Защита {10 + 30}»'
    return f'{char_name} ничего не применил'


def start_training(char_name, char_class):
    """Тренировка."""
    if char_class == 'warrior':
        print(f'{char_name}, ты Воитель — отличный боец ближнего боя.')
    if char_class == 'mage':
        print(f'{char_name}, ты Маг — превосходный укротитель стихий.')
    if char_class == 'healer':
        print(f'{char_name}, '
              f'ты Лекарь — чародей, способный исцелять раны.')
    print('Потренируйся управлять своими навыками.')
    print('Введи одну из команд: attack — чтобы атаковать противника, '
          'defence — чтобы блокировать атаку противника или special — '
          'чтобы использовать свою суперсилу.')
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
    """Описание выбранного персонажа с подтверждением."""
    approve_choice = None
    char_class = None
    while approve_choice != 'y':
        char_class = input('Введи название персонажа,'
                           ' за которого хочешь играть: '
                           'Воитель — warrior, '
                           'Маг — mage, Лекарь — healer: ')
        if char_class == 'warrior':
            print('Воитель — дерзкий воин ближнего боя. '
                  'Сильный, выносливый и отважный.')
        if char_class == 'mage':
            print('Маг — находчивый воин дальнего боя. '
                  'Обладает высоким интеллектом.')
        if char_class == 'healer':
            print('Лекарь — могущественный заклинатель. '
                  'Черпает силы из природы, веры и духов.')
        approve_choice = input('Нажми (Y), чтобы подтвердить выбор,'
                               ' или любую другую кнопку, '
                               'flake8 main.pyflake8 '
                               'main.pyчтобы выбрать '
                               'другого персонажа ').lower()
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
