
class calculator:
    def __init__(self,number_list):
        self.number_list = number_list

    def sum(self):
        total = 0
        for number in self.number_list:
            total = total + number
        return total

    def avg(self):
        total = 0
        for number in self.number_list:
            total = total + number
        avg = total/len(self.number_list)
        return avg


cal1 = calculator([1,2,3,4,5])
cal1.sum()
cal1.avg()
cal2 = calculator([6,7,8,9,10])
cal2.sum()
cal2.avg()


if __name__ == "__main__":
    print(cal1.sum())
    print(cal1.avg())
    print(cal2.sum())
    print(cal2.avg())