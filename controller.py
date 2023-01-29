import data_provider
import module 
import view
classes = {}

classes ['7А'] = {'Иванов Сергей', 'Петров Дмитрий','Сидоров Евгений'}
classes ['7Б'] = {'Дятлов Роман','Леннон Джон','Маккартни Пол'}
classes ['7В'] = {'Меркури Фредди','Джови Бон','Чайковский Петр'}
subjects = {'Математика','Литература','Химия'}
set_of_classes = {'7А','7Б','7В'}
def a_button():
        mode = '1'
        value_class = view.get_class()
        while not value_class in set_of_classes:
            print('Неправильный ввод номера класса, повторите')
            value_class = view.get_class()
        class_no = value_class + '.txt' 
        value_subject = view.get_subject()
        print(value_subject)
        while not value_subject in subjects:
            print('Неправильный ввод предмета, повторите')
            value_class = view.get_subject()
        while mode == '1':
            class_set = classes [value_class]  
            class_dict = data_provider.file_to_dict(class_set,class_no,subjects)
            print ('Текущий табель отметок')
            module.print_marks(class_dict,value_subject,classes[value_class])
            value_pupil = view.get_pupil()
            while not value_pupil in classes[value_class]:
                print('Ученик не найден, повторите ввод')
                value_pupil = view.get_pupil()
            value_mark = view.get_mark()
            while not value_mark in {'1','2','3','4','5'}:
                print('Введите оценку от 1 до 5')
                value_mark = view.get_mark()
            module.put_mark(class_dict,value_subject,value_pupil,value_mark)
            print ('Обновленный журнал')
            module.print_marks(class_dict,value_subject,classes[value_class])
            data_provider.dict_to_file(class_dict,class_no,class_set,subjects)
            print("\nЖурнал оценок обновлен")
            mode = input("Для продолжения работы с текущим журналом, введите 1, для выхода введите 0: ")        
def b_button():
    value_class = view.get_class_book()
    while not value_class in set_of_classes:
        print('Неправильный ввод номера класса, повторите')
        value_class = view.get_class_book()
     
    class_set = classes [value_class]  
    print(f"Журнал {value_class} класса:")
    class_no = value_class + '.txt' 
    class_dict = data_provider.file_to_dict(class_set,class_no,subjects)
     
    module.print_all_marks(class_dict,subjects,classes[value_class])