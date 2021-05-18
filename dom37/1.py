try :
    print ("Введите 1 для сложения")
    print ("Введите 2 для вычитания")
    print ("Введите 3 для умножения")
    print ("Введите 4 для деления")


    class Calc():

        def Sum (self, A, B):
            print (A + B)
        def Sub (self, A, B):
             print (A - B)
        def Mul (self, A, B):
            print (A * B)
        def Div (self,A, B ):
            print (A / B)   

    C = Calc()

    Input = int (input ("Сделайте выбор(1-4):"))

    if Input not in [1,2,3,4]:
        print ("Пробуй еще раз")
        exit ()

    A = int (input ("A="))
    B = int (input ("B="))

    try:
        {1: C.Sum, 2: C.Sub, 3: C.Mul, 4: C.Div}.get(Input)(A,B)
    except TypeError:
        print ("Введите значение еще раз")
        exit ()
        
except ValueError:
        "Значение не верное"