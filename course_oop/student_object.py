class studentObject():

    def __init__ (self):
        pass

    def get_avg_grades (self,grades):
        size = len(grades)
        sum  = 0
        for grade in grades:
           sum = sum +grade

        avg = sum//size
        return avg