def ordinal(number):
    if number == 1:
        return "1st"
    elif number == 2:
        return "2nd"
    elif number == 3:
        return "3rd"
    elif number >= 4:
        return f"{number}th"

count = 0
while True:
    name = (input("안녕하세요. 이름을 입력하세요: "))
    count += 1
    if count <= 10:
        print(f"Hi {name}!! You are {ordinal(count)} person come here!\n")
    else:
        print(f"Sorry {name}. The event is closed because you are {ordinal(count)} person come here\n")

