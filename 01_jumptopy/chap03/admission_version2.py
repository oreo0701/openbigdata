#coding: cp949

print("대구 IT공원 입장료 계산 프로그램 Ver. 2\n")
age=0
admission=0
preschool= "유아"
youth="어린이"
teenager="청소년"
adult="성인"
senior="노인"

free="무료"
two_thousand=2000
three_thousand=3000
five_thousand=5000

output_msg="나이를 입력하세요: "
output_fee="요금을 입력하세요: "


while True:
    print(output_msg, end='')
    customer_input = int (input())
    if customer_input >=0 and customer_input <= 3:
        print("귀하의 등급은 %s이며 입장은 %s입니다." %(preschool,free))
        break

    elif customer_input >= 4 and customer_input <= 13:
        print("귀하의 등급은 %s이며 요금은 %d원입니다." %(youth,two_thousand))
        break

    elif customer_input >= 14 and customer_input <= 18:
        print("귀하의 등급은 %s이며 요금은 %d원입니다." %(teenager,three_thousand))
        break

    elif customer_input >=19 and customer_input <= 65:
        print("귀하의 등급은 %s이며 요금은 %d원입니다." %(adult,five_thousand))
        break

    elif customer_input >= 65:
        print("귀하의 등급은 %s이며 입장이 %s입니다." %(senior,free))
        break

    elif customer_input < 0:
        print("다시 입력해 주세요.\n")
        continue

   
 #       while True:
  #          print(output_fee, end='')
   #         customer_payment = int (input())
    #            if customer_payment < 

