


#(ii)
def sum_natural_number(a,b,c,d,n):
    output=0+1+2+3+n
    print(f"The sum of natural numbers is {output}")
#Testing the function with n=4
sum_natural_number(0,1,2,3,4)


#(iii)
numbers = [1,3,5,7,9]
numbers.pop(2)

print(numbers)

#Inserting 10 at the end
numbers.append(10)
print(numbers)

#(iv)
numbers = [1,2,3,4,5,6,7,8,9,10]
for even_numbers in numbers:
    if even_numbers%2==0:
        print(even_numbers)


#(v)
# Replacing'age':20 to 25.
student_info={'name':'Alice','age':20,'grade':'A'}
student_info['age']=25
print(student_info)

#adding a new key value pair ('city':'NewYork')
student_info['city']='NewYork'
print(student_info)


#(vi)
#A new dictionary with onyly key values greater than 5
original_dict={'a':3,'b':8,'c':2,'d':7}
for x,y in original_dict.items():
    if y>5:
        new_dict=original_dict.items(y>5)
        print(new_dict)


