#coding: cp949

print("\n<대구 IT공원 입장료 계산 프로그램 Ver. 5>\n")
age=0
admission=0
customer_num =0
free_ticket=3
annual_membership=5

preschool= "유아"
youth="어린이"
teenager="청소년"
adult="성인"
senior="노인"

free="무료"
two_thousand=2000
three_thousand=3000
five_thousand=5000
card=admission*0.9

while True:
    customer_num +=1
    print("--------------------")
    print("%d번째 손님이십니다."%customer_num)
    customer_input = int (input("\n나이를 입력하세요: "))
    if customer_input >=0 and customer_input <= 3:
        print("귀하의 등급은 %s이며 입장은 %s입니다.\n" %(preschool,free))
        admission=0
        continue 
    elif customer_input >= 4 and customer_input <= 13:
        print("귀하의 등급은 %s이며 요금은 %d원입니다.\n" %(youth,two_thousand))
        admission=2000
        age=4
    
    elif customer_input >= 14 and customer_input <= 18:
        print("귀하의 등급은 %s이며 요금은 %d원입니다.\n" %(teenager,three_thousand))
        admission=3000
        age=14       
    
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
        continue          
    elif customer_input < 0:
        print("다시 입력해 주세요.\n")
        continue
  
    customer_option = int(input("요금 유형을 선택하세요. (1: 현금, 2:공원 전용 신용카드): "))


   
    
    if customer_option ==1:
        customer_payment = int(input("요금을 입력하세요: "))
        
        if customer_payment >= admission and customer_num %7 == 0 and free_tickcet > 0: 
            free_ticket -=1
            print("축하합니다. 1주년 이벤트에 당첨되었습니다. 여기 무료 티켓을 발행합니다. 잔여 무료티켓 %d\n" %free_ticket)
        elif customer_payment >= admission and customer_num %4 == 0 and annual_membership > 0:
            annual_membership -=1
            print("축하합니다. 연간회원권 구매 이벤트에 당첨되셨습니다. 연간 회원 할인 티켓을 발행합니다. 잔여 할인티켓 %d\n" %annual_membership)
        
        if customer_payment == admission:
            print("감사합니다. 티켓을 발행합니다.\n")
        elif customer_payment < admission:
            print("%d원이 모자랍니다. 투입하신 %d원을 반환합니다.\n" %(admission-customer_payment, customer_payment))
        elif customer_payment > admission:
            print("감사합니다. 티켓을 발행하고 거스름돈 %d원을 반환합니다.\n"%(customer_payment-admission))
    
    elif customer_option ==2:
        if age < 60:
            print("티켓을 발행하고 정상금액에 10%%가 할인된 %d원이 결제됩니다.\n"%(card))
            card=admission*0.9
        else :
            card=card*0.95
            print("티켓을 발행하고 장년층 5%% 추가할인이 적용된 %d원이 결제됩니다."%(card))
                
        if customer_num %7 == 0 and free_ticket > 0:
            free_ticket -=1
            print("축하합니다. 1주년 이벤트에 당첨되었습니다. 여기 무료 티켓을 발행합니다. 잔여 무료티켓 %d\n" %free_ticket)
        elif customer_num %4 == 0 and annual_membership > 0:
            annual_membership -=1
            print("축하합니다. 연간회원권 구매 이벤트에 당첨되셨습니다. 연간 회원 할인 티켓을 발행합니다. 잔여 할인티켓 %d\n" %annual_membership) 
            
         

        
        
      

