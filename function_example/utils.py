class utils():
    def avg_calc(self, value1, value2):
        print(f"calculating the avg between {value1} and {value2}")
        summary = value1 + value2
        avg = summary // 2
        if (avg > 27):
            print("avg is more than 27 ")
            avg = avg - 20
        print(f"avg value is {avg}")
        return avg

