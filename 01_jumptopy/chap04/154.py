var1 = 1 #Global Variable(전역변수) : 어디서나 접근이 가능 -> HEAP에 저장됨

def vartest(var1):          #Local Variable(지역변수): 함수 안에서만 접근이 가능. 함수가 끝나면 바로 소멸
    var1 = var1 + 1         #여기서 바로 소멸  -> stack에 저장됨

vartest(var1)

print(var1)