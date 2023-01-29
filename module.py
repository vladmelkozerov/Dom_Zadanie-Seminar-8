import data_provider
def print_marks(class_dict,subject,pupils):
        for j in pupils:
            marks_str = str(class_dict[subject][j])
            marks_str = ''.join([marks_str[i] for i in range(len(marks_str)) if (marks_str[i] != '[') and (marks_str[i] != ']') and (marks_str[i] != "'") ])
             
            print (j, marks_str,end = ' ')
        print()
def print_all_marks(class_dict,subjects,pupils):
     
    for i in subjects:
        print (f"Предмет {i}:")
        for j in pupils:
            marks_str = str(class_dict[i][j])
            marks_str = ''.join([marks_str[i] for i in range(len(marks_str)) if (marks_str[i] != '[') and (marks_str[i] != ']') and (marks_str[i] != "'") ])
             
            print (j, marks_str,end = ' ')
        print()
def put_mark(class_dict,subject,pupil,mark):
    class_dict[subject][pupil].append(mark)

