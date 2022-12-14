''' Chapter 8
Programming exercises №04
'''


def main():
    '''The main function of the module.'''

    try:

        user_line = input('Введите любую последовательность символов: ')
        user_line = user_line.upper()

        dict_en = {' ': ' ', ',': '--.--', '.': '.-.-.-', '?': '..--..',
                   '0': '-----', '1': '.----', '2': '..---', '3': '...--',
                   '4': '....-', '5': '.....', '6': '-....', '7': '--...',
                   '8': '---..', '9': '----.', 'A': '.-', 'B': '-...',
                   'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
                   'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
                   'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.',
                   'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
                   'S': '...', 'T': '-', 'U': '..-', 'V': '...-',
                   'W': '.--', 'X': '-..-', 'Y': '-.-', 'Z': '--..'
                   }
        dict_ru = {'А': '.-', 'Б': '-...', 'В': '.--', 'Г': '--.',
                   'Д': '-..', 'Е': '.', 'Ё': '.', 'Ж': '...-',
                   'З': '--..', 'И': '..', 'Й': '.---', 'К': '-.-',
                   'Л': '.-..', 'М': '--', 'Н': '-.', 'О': '---',
                   'П': '.--.', 'Р': '.-.', 'С': '...', 'Т': '-',
                   'У': '..-', 'Ф': '..-.', 'Х': '....', 'Ц': '-.-.',
                   'Ч': '---.', 'Ш': '----', 'Щ': '--.-', 'Ъ': '.--.-.',
                   'Ы': '-.--', 'Ь': '-..-', 'Э': '..-..', 'Ю': '..--',
                   'Я': '.-.-'
                   }

        out_line = ''

        for i in user_line:
            if i in dict_en:
                out_line += dict_en[i]
            elif i in dict_ru:
                out_line += dict_ru[i]

        print(out_line)

    except IOError:
        print('File not found')

    except IndexError:
        print('Indexing error')

    except:
        print('An error has occurred')


if __name__ == '__main__':
    main()
