print('Hello Middletown')

#TEST

print('Welcome') 

#TEST TEST5

num = 3
print(type(num))
# <class 'float'> 
print(3 % 2)
# 1 is the remainder 

num = 1 
num *= 10
print(num)
# 10

print(abs(-3))
# 3

print(round(3.77898))
# 4

print(round(3.75, 1))
#Will round to the first decimal so 3.8 

# Comparisons: 
# Equal: 3 == 2
# Not Equal: 3 != 2 
# Greater Than: 3 > 2
# Less Than: 3 < 2 
# Greater or Equal: 3 >= 2
# Less or Equal: 3 <= 2

num_1 = 3
num_2 = 2 

print(num_1 == num_2)
# False

print(num_1 != num_2)
# True 

num_3 = '100'
num_4 = '200' 

print(num_3 + num_4)
#100200

num_3 = int(num_3)
num_4 = int(num_4)

print(num_3 + num_4)
#300
         
print('Hello')
num = 3
print(type(num))

print(3 / 2)

print(3 ** 2)

courses = ['History', 'Math', 'Physics', 'CompSci']

cs_courses = {'History', 'Math', 'Physics', 'CompSci'}
art_courses = {'History', 'Math', 'Art', 'Design'}

print(cs_courses.union(art_courses))

student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}
print(student.get('age', 'Not Found'))



