

f=open(".\\sample.txt", 'r')
lines = f.readlines()
f.close()

total = 0
for line in lines:
    score = int(line)
    total += score

average = total/len(lines)
print("총합은 " + str(total) + "입니다.")
result="평균은 " + str(average) + "입니다."
print(result)

f=open(".\\result.txt", 'w')
f.write(result)


f.close()