''' Chapter 8
Programming exercises №01
'''


def main():
    '''The main function of the module.'''

    try:

        first_name = input('Введите своё имя с большой буквы: ')
        last_name = input('Введите свою фамилию с большой буквы: ')
        patronymic = input('Введите своё отчество с большой буквы: ')

        full_name = f'{first_name[0]}.{last_name[0]}.{patronymic[0]}'
        #full_name = full_name.upper()

        print(full_name.upper())

    except IOError:
        print('File not found')

    except IndexError:
        print('Indexing error')

    except:
        print('An error has occurred')


if __name__ == '__main__':
    main()
