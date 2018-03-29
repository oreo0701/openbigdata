number_served = 0

class Restaurant:
    def __init__(self, name, type):
        self.restaurant_name = name
        self.cuisine_type = type
    def describe_restaurant(self):
            print("저희 레스토랑 명칭은 %s 이고 %s 전문점입니다." %(self.restaurant_name, self.cuisine_type))
            input("레스토랑을 오픈하시겠습니까? (y/n)")
            if input == y:
                print("저희 %s 레스토랑이 오픈했습니다." %(self.restaurant_name))
            elif input == n:
                print("%s 문닫습니다." %(self.restaurant_name))

    def open_restaurant(self):
            print("저희 %s 레스토랑 오픈했습니다.\n" %self.restaurant_name)
    def number_served(self):


    def reset_number_served(number):
        number_served = 0
    def increment_number_served(number):
        number_served +=1

    def check_customer_number(self):
        count(number_served)
    def __del__(self):
            print("%s 레스토랑 문닫습니다." % self.restaurant_name)

choice = input("레스토랑 이름과 요리 종류를 선택하세요: ")
input_choice = choice.split()
input_name = input_choice[0]d
