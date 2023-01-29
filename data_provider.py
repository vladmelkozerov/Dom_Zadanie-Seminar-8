def file_to_dict(class_set,file,subjects):
    class_dict = {}
    class_dict['Математика'] = {}
    class_dict['Литература'] = {}
    class_dict['Химия'] = {} 
    marks = {'1','2','3','4','5'}
    with open (file,'r', encoding = "UTF-8") as file_object:
        line = file_object.read()
    lines = line.split('Предмет')
    for i in subjects:
        for k in range(len(lines)):
            if i in lines[k]:
                sub_line = lines[k].split('  ')
                for j in class_set:
                    for l in range(len(sub_line)):  
                        if j in sub_line[l]:
                            class_dict[i][j] = [sub_line[l][g] for g in range(len(sub_line[l])) if sub_line[l][g] in marks]
             
                 
    return class_dict  
def dict_to_file(class_book, file,class_set,subjects):
    with open(file, 'w', encoding = 'UTF-8') as file_object:
        for i in subjects:
            line = 'Предмет:'+i+'  '
            for j in class_set:
                line += j+ str(class_book[i][j])+'  '
            file_object.write(line+'\n')

 
