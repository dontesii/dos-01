

def lineDiff(line1, line2):
    for i in range(len(line1)):
        for y in range(len(line2)):
            if line1[i] == line2[y]:
                print('Буква= %s  Первая строка - %d, Вторая строка - %d' % (line1[i], i+1, y+1))

lineDiff(input('Введите первую строку: '), input('Введите вторую строку: '))


