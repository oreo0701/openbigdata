import time

print(time.time())

print(time.localtime(time.time()))
my_time = time.localtime(time.time())
my_time.tm_year
# print("안녕하세요. 현재 시각은 %d년 %d일 %d시 %d분 %d초입니다." %(my_time.tm_year, my_time.tm_mon, my_time.tm_mday, my_time.tm_hour, my_time.tm_min, my_time.tm_sec))

print(time.asctime(time.localtime(time.time())))
print("프로그램 종료")


print(time.strftime('%x',time.localtime(time.time())))
print(time.strftime('%c',time.localtime(time.time())))