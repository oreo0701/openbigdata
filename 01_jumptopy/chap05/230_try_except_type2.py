num1, num2 = input("두 개의 숫자를 입력하세요.").split()
result = 0

try:
    f = open('나없는파일', 'r')
    result = int(num1)/int(num2)
# except ZeroDivisionError:
except FileNotFoundError:
    print("파일이 존재하지 않습니다.")
    is_calculate = False
except ZeroDivisionError:
    print("연산을 할 수 없습니다.")
    is_calculate = False

if is_calculate:
    print("%s / %s = %d" %(num1,num2,result))
