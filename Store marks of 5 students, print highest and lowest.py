#Store marks of 5 students, print highest and lowest
dict={}
for i in range(5):
    student=input('name of student:')
    mark=float(input('enter the marks he scored:'))
    dict[student]=mark
print(dict)
highest=max(dict.values())
lowest=min(dict.values())
print('highest mark=',highest)
print('lowest mark=',lowest)