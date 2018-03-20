#coding: cp949

#pocket = ['paper', 'cellphone', 'money', 'card']
#pocket = ['paper', 'cellphone']
#pocket = ['paper']
pocket=[]

item=input("포켓에 아이템을 챙기세요: ")
#pocket.insert(0,item)  insert는 (몇 번째에, 추가할 요소) 2 argument가 필요
pocket.append(item)

if 'card' in pocket:
    print("신용카드로 택시를 탈 것을 추천합니다.")
elif 'money' in pocket:
    print("현금 이용시 영수증을 꼭 챙기세요")
elif 'cellphone' in pocket:
    print("스마트폰에 교통카드 기능이 있는지 확인하세요")
else:
    pass 
