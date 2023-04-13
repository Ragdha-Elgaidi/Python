"""
Write a program that reads 2 students information about math exam
○ For each student read: his name, id and grade
● Print the students
● Print the grades average
"""
name1 = input('Enter the first student\'s name: ')
id1 = input('Enter the first student\'s ID: ')
grade1 = float(input('Enter the first student\'s grade: '))

name2 = input('\nEnter the second student\'s name: ')
id2 = input('Enter the second student\'s ID: ')
grade2 = float(input('Enter the second student\'s grade: '))

print('\n\nInformation for students and their math grade')

msg = name1 + '(ID ' + id1 + ') got grade :' + str(grade1)

print(msg)

msg = name2 + '(ID ' + id2 + ') got grade :' + str(grade2)

print(msg)

average = (grade1 + grade2) / 2.0

print('Average math grade is', average)
