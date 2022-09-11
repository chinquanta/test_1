def step1():
    print(
        'Утка-маляр 🦆 решила выпить зайти в бар. '
        'Взять ей зонтик? ☂️'
    )
    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()
    if options[option]:
        return step2_umbrella()
    else:
        return step2_no_umbrella()

def step2_umbrella():
    print('выбрано "взять зонтик"')
    print('Странный выбор! Утке зонтик ни к чему!')

def step2_no_umbrella():
    print('выбрано "не брать зонтик"')
    print('Разумно!  Утке зонтик ни к чему!')

if __name__ == '__main__':
    step1()