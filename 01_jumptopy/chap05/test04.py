def sum(num1,num2):
    num1, num2 = input("안녕하세요. 두 수를 입력하세요.(종료: 프로그램 종료): ")
    sum=num1+num2
    return sum

try:
    sum()
except:
    print(f"죄송합니다. 첫번째(또는 두번째) 입력이 {num1}입니다. 숫자를 입력하세요 '")
