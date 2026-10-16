def generate(n):

    import string
    import random

    

    first_names = ['Susan ', 'Alfred ', 'Mildred ', 'Horatio ', 'Zeus']
    last_names = ['Green', 'Smith', 'Jones', 'Hardy', 'Drew']
    middles = list(string.ascii_uppercase)

    if n > len(first_names) * len(last_names) * len(middles):
        print('pick a number less than', len(first_names) * len(last_names) * len(middles))
        return
    
    students = []
    for first in first_names:
        for middle in middles:
            for last in last_names:
                
                student = {}                
                student['fname'] = first
                student['lname'] = last
                student['mi'] = middle
                students.append(student)

    random_students =  random.sample(students,n)

    id = 0
    for student in random_students:
        id += 1
        student['id'] = id
    return(random_students)


print(generate(100))
