''' Chapter 8
Programming exercises №08
Программа для приведения песрвых букв предложения в заглавный вид
'''


def main(sent_new=None):
    '''The main function of the module.'''

    try:

        # переменные
        count_one = 0
        sent_new = 'Вы ничего не ввели!'
        my_sentence = False

        while not my_sentence:

            if count_one >= 10:
                question_one = input('Вам не надоело?: ')
                if question_one == 'Да':
                    print('Ok! До встречи!')
                    break
                else:
                    print('Ok! Продолжим!')

            my_sentence = input('Введите текст: ')
            count_one += 1

        else:
            sent_new = ''
            sent_new += my_sentence[0].upper()

            i = 1
            while i < len(my_sentence):
                sent_new += my_sentence[i]
                if (my_sentence[i - 1] in '.!?') and my_sentence[i] == ' ':
                    sent_new += my_sentence[i + 1].upper()
                    i += 2
                else:
                    i += 1

        print(f'Исправленный текст: {sent_new}')

    except IOError:
        print('File not found')

    except IndexError:
        print('Indexing error')

    except:
        print('An error has occurred')


if __name__ == '__main__':
    main()
