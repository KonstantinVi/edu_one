''' Chapter 8
Programming exercises №09
Программа для подсчёта гласных и согласных
'''


def main(sent_new=None):
    '''The main function of the module.'''

    try:

        my_sentence = input('Введите предложение: ')
        new_sentence = ''
        var_a = 0  # переменная отвечает за подсчёт гласных
        var_b = 0  # переменная отвечает за подсчёт согласных

        for i in range(len(my_sentence)):
            if my_sentence[i].lower() in 'аоиеёуыэюя':
                new_sentence += my_sentence[i].upper()
                var_a += 1

            elif my_sentence[i].lower() in 'бвгджзйклмнпрстфхцчшщ':
                new_sentence += my_sentence[i].lower()
                var_b += 1

            else:
                new_sentence += my_sentence[i]

        print(f'Готовове предложениеЖ {new_sentence}')
        print(f'Количество гласных = {var_a}')
        print(f'Количество согласных = {var_b}')

    except IOError:
        print('File not found')

    except IndexError:
        print('Indexing error')

    except:
        print('An error has occurred')


if __name__ == '__main__':
    main()
