''' Chapter 8
Programming exercises №03
'''


def main():
    '''The main function of the module.'''

    try:

        user_data = input('Введите дату цифрами через обратный слеш: ')
        data_mass = user_data.split('/')

        month_system = ['Января', 'Февраля', 'Марта', 'Апреля',
                        'Мая', 'Июня', 'Июля', 'Августа',
                        'Сентября', 'Октября', 'Ноября', 'Декабря'
                        ]

        data_mass[1] = month_system[int(data_mass[1]) + 1]

        print(f'{data_mass[0]} {data_mass[1]} {data_mass[2]} г.')

    except IOError:
        print('File not found')

    except IndexError:
        print('Indexing error')

    except:
        print('An error has occurred')


if __name__ == '__main__':
    main()
