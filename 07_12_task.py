''' Chapter 7
Programming exercises №12
'''

from math import sqrt


def main():
    '''The main function of the module.'''

    def natur_numer(numer):
        '''Natural number'''

        rezult = True
        a = round(sqrt(numer))

        if numer != 2:
            for i in range(2, a + 1):
                if (numer % i) == 0:
                    rezult = False

        return rezult

    numer = int(input('Введите натуральное число: '))
    a_mass = [i for i in range(1, numer + 1)]
    b_mass = []

    for i in a_mass:
        if natur_numer(i):
            b_mass.append(i)

    print(*b_mass)


if __name__ == '__main__':
    main()
