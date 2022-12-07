''' Chapter 8
Programming exercises №06
Программа для подсчёта среднего количества слов в предложениях, которые
взяты из конкретного файла. По условию: одно предложение на одной строке.
'''


def main():
    '''The main function of the module.'''

    try:

        a_mass = []
        b_mass = []

        open_file_ = open(r'D:\Python\Work_01\edu_one\text.txt', 'r')

        read_open_file = open_file_.readline()
        read_open_file = read_open_file.rstrip('\n')
        new_line = read_open_file.split()

        while read_open_file != '':
            read_open_file = read_open_file.rstrip('\n')
            new_line = read_open_file.split()

            for i in range(len(new_line)):
                new_line[i] = new_line[i].strip(',')
                new_line[i] = new_line[i].strip('.')
                new_line[i] = new_line[i].strip('!')
                new_line[i] = new_line[i].strip('?')

                if not new_line[i].isdigit():
                    a_mass.append(new_line[i])

            b_mass.append(len(a_mass))
            a_mass = []

            read_open_file = open_file_.readline()

        open_file_.close()

        print(b_mass)

        print(f'Среднее количество слов в предложениях: {sum(b_mass) / len(b_mass)}')

    except IOError:
        print('File not found')

    except IndexError:
        print('Indexing error')

    except:
        print('An error has occurred')


if __name__ == '__main__':
    main()
