from pprint import pprint

# data structure list of dictionaries
students = [
    {'fname': 'Bob', 'lname': 'Green',
     'quiz': [100, 90, 80, 70, 60, 50],
     'labs': [100, 90, 95, 100],
     'pb': True},

    {'fname': 'Alice', 'lname': 'Smith',
     'quiz': [99, 85, 88, 92, 87, 91],
     'labs': [95, 90, 100, 5],
     'pb': True},

    {'fname': 'Carlos', 'lname': 'Lopez',
     'quiz': [75, 80, 70, 85, 90, 78],
     'labs': [80, 85, 90, 88],
     'pb': False},

    {'fname': 'Emma', 'lname': 'Brown',
     'quiz': [98, 95, 100, 92, 96, 94],
     'labs': [100, 100, 95, 98],
     'pb': True},

    {'fname': 'David', 'lname': 'Jones',
     'quiz': [65, 70, 72, 68, 75, 80],
     'labs': [70, 75, 80, 78],
     'pb': False},

    {'fname': 'Sophia', 'lname': 'Lee',
     'quiz': [88, 92, 85, 90, 94, 89],
     'labs': [90, 95, 92, 100],
     'pb': True},

    {'fname': 'James', 'lname': 'Wilson',
     'quiz': [82, 78, 85, 80, 88, 84],
     'labs': [85, 80, 90, 88],
     'pb': False},

    {'fname': 'Maya', 'lname': 'Patel',
     'quiz': [100, 98, 95, 100, 97, 99],
     'labs': [100, 98, 100, 100],
     'pb': True},

    {'fname': 'Ryan', 'lname': 'Taylor',
     'quiz': [55, 60, 65, 70, 68, 72],
     'labs': [65, 70, 75, 80],
     'pb': False},

    {'fname': 'Olivia', 'lname': 'Martin',
     'quiz': [92, 88, 94, 90, 91, 95],
     'labs': [95, 100, 90, 98],
     'pb': True}
]








grades = []

# calculate average of list
def average(some_list: list)-> float:
    total = 0
    for num in some_list:
        total += num
    return total / len(some_list)

# get grade for each student -> return dictionary
def get_grade(pupil: dict) -> dict:
    
    student = {}
    student['name'] = pupil['fname'] + ' ' + pupil['lname']

    avg_quiz = average(pupil['quiz'])
    avg_labs = average(pupil['labs'])

    student['grade'] = round(.3 * avg_quiz + .7 * avg_labs, 2)
    return student

for student in students:
    pupil = get_grade(student)
    grades.append(pupil)

pprint(grades, sort_dicts=False)