class Restaurant:
    def __init__(self, name, type):
        self.restaurant_name = name
        self.cuisine_type = type
    def describe_restaurant(self):
            print("저희 레스토랑 명칭은 %s 이고 %s 전문점입니다." %(self.restaurant_name, self.cuisine_type))
            input("레스토랑을 오픈하시겠습니까? (y/n)")
                if input == y:
                    pass
                elif input == n:

    def open_restaurant(self):
            print("저희 %s 레스토랑 오픈했습니다.\n" %self.restaurant_name)
    def number_served(self):
            pass
    def __del__(self):
            print("%s 레스토랑 문닫습니다." % self.restaurant_name)

choice = input("레스토랑 이름과 요리 종류를 선택하세요: ")
input_choice1 = choice.split()
input_name1 = input_choice1[0]
input_type1 = input_choice1[1]

restaurant1 = Restaurant(input_name1,input_type1)
restaurant1.describe_restaurant()
restaurant1.open_restaurant()

choice = input("레스토랑 이름과 요리 종류를 선택하세요: ")
input_choice2 = choice.split()
input_name2 = input_choice2[0]
input_type2 = input_choice2[1]

restaurant2 = Restaurant(input_name2,input_type2)
restaurant2.describe_restaurant()
restaurant2.open_restaurant()

choice = input("레스토랑 이름과 요리 종류를 선택하세요: ")
input_choice3 = choice.split()
input_name3 = input_choice3[0]
input_type3 = input_choice3[1]

restaurant3 = Restaurant(input_name3,input_type3)
restaurant3.describe_restaurant()
restaurant3.open_restaurant()
print("저녁 10시가 되었습니다.\n")