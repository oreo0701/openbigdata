import csv
import math



def close_program(program):
    if program == '0':
        print("프로그램을 종료 합니다.")
    return program

def show_column_instance(col_name):
    col_instance = []
    col_index = data[0].index(col_name)

    for row in data[1:]:
        col_instance.append(row[col_index])
    print(col_instance)

def show_row_instance(row_key):
    for row in data:
        if row_key in row:
            for row_element in row:
                print(row_element)

def show_total(col_name):
    col_instance = []
    col_index = data[0].index(col_name)

    if type(col_name) == "str":
        list(map(int,col_name))

    elif type(col_name) == "float":
        list(map(float,col_name))

    for row in data[1:]:
        col_instance.append(row[col_index])
    print(type(col_instance))

    print(sum(col_instance))


with open("Demographic_Statistics_By_Zip_Code.csv", newline='')as infile:
    data = list(csv.reader(infile))

print("<CSV Handle 연습예제>\n0.종료 1.행 2.열 3.총합 4.평균 5.최대값 6.최소값 7.편차 9.분산 10.오름차순 정렬 11.내림차순 정렬")

while True:
    menu=input("\n메뉴를 선택하세요: ")
    menu_choice = int(menu)
    access_input = input("Access Key 를 입력하세요: ")

    if menu_choice == 1:
        show_row_instance(access_input)
        continue
    elif menu_choice == 2:
        show_column_instance(access_input)
        continue
    elif menu_choice == 3:
        show_total(access_input)
        continue