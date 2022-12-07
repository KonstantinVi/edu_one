''' Chapter 7
Programming exercises №12
'''

import random


def main():
    '''The main function of the module.'''

    file_list = open(r'D:\Python\Work_01\edu_one\8_ball_responses_ru.txt', 'r')
    file_line = file_list.readline()

    a_mass = []

    while file_line != '':
        file_line = file_line.rstrip('\n')
        a_mass.append(file_line)
        file_line = file_list.readline()

    while True:
        question = input('''Введите свой вопрос,
        Либо нажмите 'д', 
        чтобы остановить данный опрос: ''')

        if question != 'д':
            index_a_mass = random.randint(0, (len(a_mass)-1))
            print(a_mass[index_a_mass])
        else:
            print('Вы решили выйти из программы!')
            break

    file_list.close()

if __name__ == '__main__':
    main()
