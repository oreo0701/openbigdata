class Restaurant:
    def __init__(self, name, type):
        self.restaurant_name = name
        self.cuisine_type = type
    def describe_restaurant(self):
            print("저희 레스토랑 명칭은 %s 이고 %s 전문점입니다." %(self.restaurant_name, self.cuisine_type))
    def open_restaurant(self):
            print("저희 %s 레스토랑 오픈했습니다. 어서오세요." %self.restaurant_name)


choice = input("레스토랑 이름과 요리 종류를 선택하세요: ")
input_choice = choice.split()
input_name = input_choice[0]
input_type = input_choice[1]

restaurant = Restaurant(input_name,input_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()
