# Make a list of ten students in your class.
# Print the name of each student whose name starts with ‘B’.

# making the list of ten students in my class

list_of_students = ['hari','shyam','Bibek',
                    'Bishal','anup','aditya',
                    'safal','abhaya','arun','sita']

for i in list(list_of_students):
    if i.startswith('B'):
        print(i)

