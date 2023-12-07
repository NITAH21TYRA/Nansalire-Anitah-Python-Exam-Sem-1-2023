#Section B 
#Question 3
#(i)
def age():
    age=int(input('Enter your age:'))
    if age>=18:
        print('You are eligible')
    else:
        print('You are not eligible')
age()


#(ii)
def grade_students():
    mark=int(input('Enter your mark:'))
    if mark>=90:
        print('A')
    elif mark>=80 and mark<=89:
        print('B')
    elif mark>=70 and mark<=79:
        print('C')
    elif mark>=60 and mark<=69:
        print('D')
    else:
        print('F')
grade_students()

#(iii)
# Testing the function with an 85 mark.

def grade_students():
    mark=85
    if mark>=90:
        print('A')
    elif mark>=80 and mark<=89:
        print('B')
    elif mark>=70 and mark<=79:
        print('C')
    elif mark>=60 and mark<=69:
        print('D')
    else:
        print('F')
grade_students()


#(iv)
def grade_students():
    mark=int(input('Enter your mark:'))
    if mark>=90:
        print('A')
    elif mark>=80 and mark<=80:
        print('B')
    elif mark>=70 and mark<=79:
        print('C')
    elif mark>=60 and mark<=69:
        print('D')
    else:
        print('F')
grade_students()

#(v)
def grade_students():
    mark=int(input('Enter your mark:'))
    if mark>=90:
        print('A')
        print('Exellent')
    elif mark>=80 and mark<=80:
        print('B')
        print('Exellent')
    elif mark>=70 and mark<=79:
        print('C')
        print('Good')
    elif mark>=60 and mark<=69:
        print('D')
        print('Satisfactory')
    else:
        print('F')
        print('Needs improvement')
grade_students()

#Testing for the mark of 78
def grade_students():
    mark=78
    if mark>=90:
        print('A')
        print('Exellent')
    elif mark>=80 and mark<=80:
        print('B')
        print('Exellent')
    elif mark>=70 and mark<=79:
        print('C')
        print('Good')
    elif mark>=60 and mark<=69:
        print('D')
        print('Satisfactory')
    else:
        print('F')
        print('Needs improvement')
grade_students()