#coding: cp949

print("----택시 안내 가이드 프로그램 ver1----")

#money = 2000
#card = False
#print("가지고 계신 금액을 입력하세요: ",end='')
money=int(input("가지고 계신 금액을 입력하세요:" ))
card=int(input("신용카드를 소지하고 계십니까? (1: 예, 2:아니오)"))


print("입력 조건 분석")
print("\n현재 가지고 계신 금액은 "+str(money)+"원 입니다.")

if card ==1 :
    print("신용카드를 소지하고 계십니다.")
else:
    print("현재 소지하고 계신 신용카드가 없습니다.")

print("\n분석 결과")
if money >= 3000 or card==1 :
    print("택시를 타고 가실 수 있습니다.")
else:
    print("걸어 가시는게 낫겠네요")

print("\n저희 택시 안내 프로그램을 이용해 주셔서 감사합니다.")

