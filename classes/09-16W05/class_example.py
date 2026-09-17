from pprint import pprint
students = []

fname = 'fname'
lname = 'lname'
quiz = 'quiz'
labs = 'labs'
pb = 'pb'
student = {fname:'bob',lname:'green',quiz: [100,90,80,70,60,50], labs:[100,90,95,100], pb:True}
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

for student in students:
    pupil = {}

    pupil['name']= student['fname'] + ' ' + student['lname']

    totalq = 0
    for testq in student['quiz']:        
        totalq += testq      # total = total + test
    avgq =  totalq / len(student['quiz'])

    totall = 0
    for testl in student['labs']:            
        totall += testl      # total = total + test    
    avgl =  totall / len(student['labs'])

    pupil['grade'] = round(.3 * avgq + .7 * avgl, 2)
    
    grades.append(pupil)

pprint(grades, sort_dicts=False)