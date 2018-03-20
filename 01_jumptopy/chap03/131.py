#coding: cp949
student_name_lists = [
        ('유','영재'),
        ('문','희식'),
        ('김','광훈'),
        ('이','효진'),
        ('문','재인'),
        ]

searching_last_name=input("검색하고자 하는 성을 입력하세요: ")
is_found_flag = False
for (last_name,first_name) in student_name_lists:
    if searching_last_name == last_name:
        if is_found_flag == False:
            print("<<검색결과>>")        
            is_found_flag = True       
        print(last_name + first_name)
         

