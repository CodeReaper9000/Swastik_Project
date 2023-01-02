path='C:/PythonProgrammingProject_main-folder'

def createfile(name,lst):
    with open(f'{path}/{name}','a',newline='')as f:
        script= csv.writer(f)
        script.writerow(lst)
        print(f"{name} file has been UPDATED")


createfile('Department.csv',['Department ID','Department Name','List of Batches'])
createfile('Batch.csv',['Batch ID','Batch Name','Department Name','List of Courses','List of Students'])
createfile('Course.csv',['Course ID','Course Name','Marks Obtained'])
createfile('Student.csv',['Student ID','Name','Class Roll Number','Batch ID'])
createfile('Examination.csv',['Course Name','Student ID','Marks'])

#Department
d_no = int(input("Enter number of departments:"))
depart_id = []
depart_name = []
for i in range(d_no):
    depart_id.append(input("Enter department ID(eg:CSE):"))
    depart_name.append(input("Enter department Name:"))

#Batch
b_no = int(input("Enter number of batches:"))
batch_id = []
batch_name = []
for i in range(b_no):
    year = input("Enter batch year(Eg:2022-26):")
    print(depart_id)
    batch_depart = input("Choose department:")
    batch_id.append(batch_depart+year[2:4])
    batch_name.append(batch_depart+" "+year)

#course
c_no = int(input("Enter number of courses:"))
course_id = []
course_name = []
for i in range(c_no):
    course_id.append(input("Enter course ID(eg:C001):"))
    course_name.append(input("Enter course name(eg:Python Programming):"))

#student
s_no = int(input("Enter number of students:"))
student_name = []
student_id = []
student_roll = []
for i in range(s_no):
    print(batch_id)
    student_batch = input("Choose batch id student belongs to:")
    student_name.append(input("Enter name of student:"))
    student_roll.append(input("Enter roll number(eg:01):"))
    student_id.append(student_batch+student_roll[i])

