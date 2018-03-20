#coding: cp949

print("대구 IT공원 입장료 계산 프로그램 Ver. 4\n")
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
output_option="요금 유형을 선택하세요. (1: 현금, 2:공원 전용 신용카드): "

while True:
    print(output_msg, end='')
    customer_input = int (input())
    if customer_input >=0 and customer_input <= 3:
        print("귀하의 등급은 %s이며 입장은 %s입니다.\n" %(preschool,free))
        age =0
        admission=0
    
    elif customer_input >= 4 and customer_input <= 13:
        print("귀하의 등급은 %s이며 요금은 %d원입니다.\n" %(youth,two_thousand))
        age =4
        admission=2000
        
    elif customer_input >= 14 and customer_input <= 18:
        print("귀하의 등급은 %s이며 요금은 %d원입니다.\n" %(teenager,three_thousand))
        age=14
        admission=3000
        
    elif customer_input >=19 and customer_input <= 59:
        print("귀하의 등급은 %s이며 요금은 %d원입니다.\n" %(adult,five_thousand))
        age=19
        admission=5000
        
    elif customer_input >=60 and customer_input <= 65:
        print("귀하의 등급은 %s이며 요금은 %d원입니다.\n" %(adult,five_thousand))
        age=60
        admission=5000

    elif customer_input >= 66:
        print("귀하의 등급은 %s이며 입장이 %s입니다.\n" %(senior,free))
        age=65
        admission=0
        
    elif customer_input < 0:
        print("다시 입력해 주세요.\n")
        continue
    
    while age >0 and age <65 :
        card=admission*0.9
        print(output_option, end='')
        customer_option = int(input())
       
        if customer_option ==1:
            print(output_fee, end='')
            customer_payment = int(input())
            
            if customer_payment == admission:
                print("감사합니다. 티켓을 발행합니다.\n")
                break
            elif customer_payment < admission:
                print("%d원이 모자랍니다. 투입하신 %d원을 반환합니다.\n" 
                %(admission-customer_payment, customer_payment))
                break
            elif customer_payment > admission:
                print("감사합니다. 티켓을 발행하고 거스름돈 %d원을 반환합니다.\n" 
                %(customer_payment-admission))
                break
        elif customer_option ==2:
            if age < 60:
                print("티켓을 발행하고 정상금액에 10%%가 할인된 %d원이 결제됩니다.\n"%(card))
                card=admission*0.9
                break            
            else :
                card=card*0.95
                print("티켓을 발행하고 장년층 5%% 추가할인이 적용된 %d원이 결제됩니다."
                    %(card))
                break
    break
      

