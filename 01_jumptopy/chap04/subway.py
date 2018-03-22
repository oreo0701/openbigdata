
print("안녕하세요. 저희 가게를 방문해 주셔서 감사합니다.")
menu = int(input("1. 주문 \n2. 종료\n메뉴를 선택해주세요: "))
ingredient_list=[]


def input_ingredient(menu):
    if menu == 1:
        while True:
            ingredient = input("원하시는 재료를 입력하세요: ")
            if ingredient == '종료':
                break
            else:
                ingredient_list.append(ingredient)
    elif menu == 2:
        return ingredient_list

def make_sandwiches(ingredient_list):
    if menu == 1:
        print("샌드위치를 만들겠습니다")
        for b in ingredient_list:
            print("%s를 추가합니다" %b)
        print("여기 주문하신 샌드위치 만들었습니다. 맛있게 드세요")
    else:
        print("이용해주셔서 감사합니다")

input_ingredient(menu)
make_sandwiches(ingredient_list)