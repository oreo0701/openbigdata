import urllib.request
import urllib.parse
import datetime
import json
import requests

g_Radiator = False
g_Gas_Valve = False
g_Balcony_Windows = False
g_Door = False
g_AI_Mode = False

def print_main_menu():
    print("\n1. 장비상태 확인")
    print("2. 장비제어")
    print("3. 스마트모드")
    print("4. 날씨 확인")
    print("5. 시뮬레이션모드")
    print("6. 프로그램 종료")


def print_device_status(device_name,devcie_status):
    print("%s 상태: "%device_name, end="")
    if devcie_status == True : print("작동")
    else: print("정지")

def check_device_status():
    print_device_status('난방기',g_Radiator)
    print_device_status('가스밸브', g_Gas_Valve)
    print_device_status('발코니(베란다) 창문', g_Balcony_Windows)
    print_device_status('출입문 상태', g_Door)

def print_device_menu():
    print("\n상태 변경할 기기를 선택하세요.")
    print("1. 난방기")
    print("2. 가스밸브")
    print("3. 발코니(베란다)창")
    print("4. 출입문")

def control_device():
    global g_Radiator, g_Gas_Valve, g_Balcony_Windows, g_Door

    check_device_status()
    print_device_menu()
    menu_num = int(input("번호를 입력하세요: "))

    if menu_num == 1: g_Radiator = not g_Radiator
    if menu_num == 2: g_Gas_Valve = not g_Gas_Valve
    if menu_num == 3: g_Balcony_Windows = not g_Balcony_Windows
    if menu_num == 4: g_Door = not g_Door

    check_device_status()

#################
def get_request_url(url):
    req=urllib.request.Request(url)

    try:
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            print("[%s] URL Request Success" %datetime.datetime.now())
            return response.read().decode('utf-8')
    except Exception as e:
        print(e)
        print("[%s] Error for URL: %S"%(datetime,datetime.now(),url))
        return None
########################

def get_realtime_weather_info():
    request_data()
    write_open_json_file()
    RM1_info()

def request_data():
    # current time
    now = datetime.datetime.now()
    base_date = str(now.year) + str(now.month) + str(now.day)
    base_time = str(now.hour) + str(now.minute)

    # location
    x = 89
    y = 91

    # private key
    service_key = "Jvg5WLwXnf%2BbDrFmoNYHyoyudFYNVMBCwr375OfMUGIpwDuEIdM422XY%2BhVy60RhSeCKQXRFAVRauGlP%2B5xsYg%3D%3D&numOfRows=30"
    url = f"http://newsky2.kma.go.kr/service/SecndSrtpdFrcstInfoService2/ForecastTimeData?base_date={base_date}&base_time={base_time}&nx={x}&ny={y}&_type=json&ServiceKey={service_key}"

    # request data
    req = urllib.request.Request(url)
    response = urllib.request.urlopen(req)
    reDate = json.loads(response.read().decode('utf8'))




def smart_mode():
    global g_AI_Mode
    print("1. 인공지능 모드 조회")
    print("2. 인공지능 모드 상태 변경")
    print("3. 실시간 기상정보 Update")
    menu_num = int(input("메뉴를 선택하세요: "))

    if menu_num == 1:
        print("현재 인공지능 모드: ", end='')
        if g_AI_Mode == True: print("작동")
        else:print("중지")
    if menu_num == 2:
        g_AI_Mode = not g_AI_Mode
        print("현재 인공지능 모드: ", end='')
        if g_AI_Mode == True: print("작동")
        else: print("중지")
    elif menu_num == 3:
        get_realtime_weather_info()

print("<스마트 홈네트워크 시뮬레이션 프로그램 ver 1.0>")
print("                                 - 이현구 -")

def simulation_mode():
    pass

def RM1_info():
    global json_big_data
    a = json_big_data["response"]
    b = a["body"]
    c = b["items"]
    value_item = c['item']

    for value in value_item:
        if value["category"] == "RN1":
            RN1_id = value["category"]
            if value['fcstValue'] == 0:
                print("예상 강수량은 0mm 입니다.")
            elif value['fcstValue'] == 1:
                print("예상 강수량은 1mm 미만 입니다.")
            elif value['fcstValue'] == 5:
                print("예상 강수량은 1~4mm 입니다.")
            elif value['fcstValue'] == 10:
                print("예상 강수량은 5~9mm 입니다.")
            elif value['fcstValue'] == 20:
                print("예상 강수량은 10~19mm 입니다.")
            elif value['fcstValue'] == 40:
                print("예상 강수량은 20~39mm 입니다.")
            elif value['fcstValue'] == 70:
                print("예상 강수량은 40~69mm 입니다.")
            elif value['fcstValue'] == 100:
                print("예상 강수량은 70mm이상 입니다.")
        else:
            pass
    print("예상 강수량은 " + str(RM1) + "mm 입니다.")

### write json file
def write_open_json_file():
    with open("weather_forecast.json", 'w', encoding='utf-8') as json_data:
        retJson=json.dumps(reDate, indent=4, sort_keys=True,ensure_ascii=False)
        json_data.write(retJson)

## open json file
    with open("weather_forecast.json",encoding='UTF8') as json_file:
        json_object = json.load(json_file)
        json_string = json.dumps(json_object)
        json_big_data = json.loads(json_string)


while True:
    print_main_menu()
    menu_num = int(input("메뉴를 선택하세요: "))

    if(menu_num == 1):
        check_device_status()
    elif(menu_num ==2):
        control_device()
    elif(menu_num == 3):
        smart_mode()
    elif(menu_num == 4):
        get_realtime_weather_info()
    elif(menu_num == 5):
        simulation_mode()
    elif(menu_num == 6):
        break


