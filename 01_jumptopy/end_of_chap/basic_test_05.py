#<추가 실습>
# 상속의 개념을 활용해서 레스토랑 클래스 작성하시오
# Super Class: 레스토랑의 공통 속성 및 행위 정의
# Child Class: 레스토랑에 특화된 속성과 행위 정의 (2개만 정의)

class Restaurant:
    def __init__(self,name,type,price):
        self.name=name
        self.typ=type
        self.price=price
    def desc_restaurant(self,name,type):
        print(f'저희 {name} 레스토랑은 {type}을 판매합니다.')
    def price_restaurant(self,name,price):
        print(f'{name} 레스토랑의 음식 가격은 {price}입니다')

class Thai_Restaurant(Restaurant):
    def specialty(self,name,type):
        print(f'저희 {name} 레스토랑은 {type}요리를 전문으로 합니다.')
    def break_time(self,name):
        print(f'{name} 레스토랑의 휴식시간은 3시~4시 입니다')



