''' Глава 7
Упражнения для программирования №6
'''


def main():
    ''' Главная функция модуля
    '''

    def abc(a, b):
        '''Функция расчёта большего'''
        c = []
        for i in a:
            if i > b:
                c.append(i)
        return c

    a_mass = list(
        map(int, input('Введите нескольно целыхчисел через пробел: ').split()))
    n = int(input('Введите одно целое число: '))

    print(*abc(a_mass, n))


if __name__ == '__main__':
    main()
