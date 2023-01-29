import controller
finish = '1'
while not finish == '0' :
    controller.a_button()
    finish = input("\n Для завершения работы с журналом введите 0, для продолжения работы с журналом введите 1, для вывода журнала класса по всем предметам, введите 3: ") 
    if finish == '3':
        controller.b_button()
 
print ("\nРабота с журналом завершена")


