# coding: cp949
order_list = [
        "짜장면2",
        "짬뽕2", 
        "짜장면1",
        "짬짜면2",
        "팔보채+볶음밥2",
        "삭스핀1+볶음밥1"]
print("""오픈 반점에 오신 것을 환영합니다.
지금까지 주문리스트입니다.""")
print(order_list)

print("\n지금부터 요리를 시작하겠습니다.")
while order_list:
    print("'"+order_list.pop(0)+"' 요리가 완료되었습니다.")

print("\n모든 주문에 대하여 처리하였습니다.")

