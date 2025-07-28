class courseObject():

    def __init__ (self,course_name,course_code,pass_point=50):
        self.course_name = course_name
        self.course_code = course_code
        self.pass_point = pass_point
        print  (f"into init course, name is {self.course_name},course code  is {self.course_code}")



    def get_free_slots(self,max_slotes,current_slotes):
        free_slotes = max_slotes - current_slotes
        if free_slotes>0 :
            return free_slotes
        else:
            return -1

    def print_course_details (self):
        print  (f"course name is {self.course_name},course code  is {self.course_code}")


    def get_student_pass (self,student_avg_grade):
        if student_avg_grade > self.pass_point:
            print (f"{student_avg_grade} is above the pass point")
            return True
        else:
            print (f"{student_avg_grade} is less than pass point")

            return False