import random
ver = 0
print("Камень давит ножницы. Ножницы режут бумагу. Бумага накрывает камень.")
while (ver == 0):   
        x = int(input("1 - камень, 2 - ножницы, 3 - бумага. Твой выбор- "   ))
        if (x == 1 or x == 2 or x == 3):
            ver = 1    
if x == 1:        print("Вы вооружились камнем.")  
if x == 2:        print("Вы вооружились ножницами.") 
if x == 3:        print("Вы вооружились бумагой.")  
comp = random.randint(1, 3)
if comp == 1:     print("Компьютер вооружился камнем.") 
if comp == 2:     print("Компьютер вооружился ножницами.")
if comp == 3:     print("Компьютер вооружился бумагой.")

if x == 1 and comp == 2:        win = 1 
if x == 1 and comp == 3:        win = 2 
if x == 2 and comp == 1:        win = 2  
if x == 2 and comp == 3:        win = 1 
if x == 3 and comp == 1:        win = 1
if x == 3 and comp == 2:        win = 2
if x == comp:                   win = 0
if win == 0:        print("Ничья!")
if win == 1:        print("Вы победили")
#player_score = player_score + 1
if win == 2:        print("Победил компьютер!")
#computer_score + 1
    