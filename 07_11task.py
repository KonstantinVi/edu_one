''' Chapter 7
Programming exercises №11
'''

import random


def main():
    '''The main function of the module.'''

    def random_square():
        '''Function creates a list'''
        a_mass = []
        while len(a_mass) < 9:
            a = random.randint(1, 9)
            if a not in a_mass:
                a_mass.append(a)
            else:
                continue
        b_mass = []
        for i in range(0, 9, 3):
            b_mass.append(a_mass[i:i + 3])
        return b_mass

    a_mass = random_square()
    a0 = sum(a_mass[0])
    a1 = sum(a_mass[1])
    a2 = sum(a_mass[2])
    a3 = sum([a_mass[0][0], a_mass[1][0], a_mass[2][0]])
    a4 = sum([a_mass[0][1], a_mass[1][1], a_mass[2][1]])
    a5 = sum([a_mass[0][2], a_mass[1][2], a_mass[2][2]])
    a6 = sum([a_mass[0][0], a_mass[1][1], a_mass[2][2]])
    a7 = sum([a_mass[0][2], a_mass[1][1], a_mass[2][0]])

    if a0 == a1 == a2 and a2 == a3 == a4 and a4 == a5 == a6 == a7:
        print('Квадрат Ло Шу!')
        print(*a_mass, sep='\n')
    else:
        print('Просто квадрат!')
        print(*a_mass, sep='\n')


if __name__ == '__main__':
    main()
