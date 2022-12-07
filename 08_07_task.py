''' Chapter 8
Programming exercises №07
Программа для подсчёта:
+ количества букв в верхнем регистре
+ количество букв в нижнем регистре
+ количество цифр
+ количество пробельных символов
'''


def main():
    '''The main function of the module.'''

    try:

        a_mass = [0, 0, 0, 0]  # верхний, нижний, цифра, пробел

        A = 0
        a = 0
        digit = 0
        space_a = 0

        open_file_ = open(r'D:\Python\Work_01\edu_one\text.txt', 'r')

        read_open_file = open_file_.readline()
        read_open_file = read_open_file.rstrip('\n')

        while read_open_file != '':

            read_open_file = read_open_file.rstrip('\n')

            for i in read_open_file:
                if i.isalpha():
                    if i.isupper():
                        A += 1
                    elif i.lower():
                        a += 1
                elif i.isdigit():
                    digit += 1
                elif i.isspace():
                    space_a += 1

            a_mass[0] += A
            a_mass[1] += a
            a_mass[2] += digit
            a_mass[3] += space_a

            A = 0
            a = 0
            digit = 0
            space_a = 0

            read_open_file = open_file_.readline()

        open_file_.close()

        print(f'Количества букв в верхнем регистре: {a_mass[0]}')
        print(f'Количество букв в нижнем регистре: {a_mass[1]}')
        print(f'Количество цифр: {a_mass[2]}')
        print(f'Количество пробельных символов: {a_mass[3]}')

    except IOError:
        print('File not found')

    except IndexError:
        print('Indexing error')

    except:
        print('An error has occurred')


if __name__ == '__main__':
    main()
