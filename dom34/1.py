a = input('Введи строку : ')
glas = 'aeyuoi'
b = []
for i in a:
    if i in glas:
        b.append(i)
print('гласных :',len(b))
