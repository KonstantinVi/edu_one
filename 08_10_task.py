''' Chapter 8
Programming exercises №10
Программа для подсчёта самого частого символа
'''


def main(sent_new=None):
    '''The main function of the module.'''

    try:

        char_one = 0  # счётчик количества повторений буквы в тексте
        max_number = 0  # максимальное количество повторений одной буквы
        one_word = input('Введите любое предложение: ')

        while one_word != '':
            one_letter = one_word[0].lower()

            for i in one_word:
                if i.lower() != one_letter:
                    two_word += i
                else:
                    char_one += 1

            if char_one >= max_number:
                two_letter = one_letter
                max_number = char_one

            char_one = 0
            one_word = two_word
            two_word = ''

        print(
            f'Буква с максимальным повтором {two_letter}, повторов {max_number}')


    except IOError:
        print('File not found')

    except IndexError:
        print('Indexing error')

    except:
        print('An error has occurred')


if __name__ == '__main__':
    main()
