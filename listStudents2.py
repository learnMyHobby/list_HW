#Make a list of ten students in your class. Print the name of
# each student whose name ends with ‘a’.

listStudents = ['hari','shyam','Bibek',
                'Bishal','anup','aditya',
                'safal','abhaya','arun','sita']

for i in list(listStudents):
    if i.startswith('a'):
        print(i)