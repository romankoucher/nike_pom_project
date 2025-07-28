from course_oop.course_object import courseObject
from course_oop.student_object import studentObject

course_1=courseObject("English","123abc",60)
course_2=courseObject("Math","640")

student_1=studentObject()
student_2=studentObject()

grades_2 =[60,45,36,77,88,90,100]
avg_2 = student_2.get_avg_grades(grades_2)

grades_1 =[22,45,36,77,11,34,11]
avg_1 = student_1.get_avg_grades(grades_1)

course_1.get_student_pass(avg_1)
course_2.get_student_pass(avg_1)
course_1.get_student_pass(avg_2)
course_1.get_student_pass(avg_2)
course_1.get_student_pass(77)



print ("test end")