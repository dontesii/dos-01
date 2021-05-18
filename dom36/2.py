def wer(x,y):

    if ( x% 2==0) and (y % 2== 0):      
           x=print("Оба числа четные")
    elif (x%2!=0) and (y%2!=0):      
          x=print("Оба числа нечетные")
    else:
        x=print("Разница чисел = ", x-y)
    return x

x=int(input("Число Х: "))
y=int(input("Число Y: "))
wer(x,y)