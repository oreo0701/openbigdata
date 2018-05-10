import urllib.request
import json
import datetime

#current time
now = datetime.datetime.now()
base_date=str(now.year)+str(now.month)+str(now.day)
base_time=str(now.hour)+str(now.minute)

# location
x=89
y=91

# private key
service_key="Jvg5WLwXnf%2BbDrFmoNYHyoyudFYNVMBCwr375OfMUGIpwDuEIdM422XY%2BhVy60RhSeCKQXRFAVRauGlP%2B5xsYg%3D%3D&numOfRows=30"

url=f"http://newsky2.kma.go.kr/service/SecndSrtpdFrcstInfoService2/ForecastTimeData?base_date={base_date}&base_time={base_time}&nx={x}&ny={y}&_type=json&ServiceKey={service_key}"

# request data
req=urllib.request.Request(url)
response=urllib.request.urlopen(req)
reDate=json.loads(response.read().decode('utf8'))

### write json file
with open("weather_forecast.json", 'w', encoding='utf-8') as json_data:
    retJson=json.dumps(reDate, indent=4, sort_keys=True,ensure_ascii=False)
    json_data.write(retJson)

### open json file
with open("weather_forecast.json",encoding='UTF8') as json_file:
    json_object = json.load(json_file)
    json_string = json.dumps(json_object)
    json_big_data = json.loads(json_string)

a=json_big_data["response"]
b=a["body"]
c=b["items"]
value_item=c['item']

for value in value_item:
    if value["category"] == "RN1":
        RN1_id = value["category"]
        if value['fcstValue'] == 0:
            print("예상 강수량은 0mm 입니다.")
        elif value['fcstValue'] ==1:
            print("예상 강수량은 1mm 미만 입니다.")
        elif value['fcstValue'] ==5:
            print("예상 강수량은 1~4mm 입니다.")
        elif value['fcstValue'] ==10:
            print("예상 강수량은 5~9mm 입니다.")
        elif value['fcstValue'] ==20:
            print("예상 강수량은 10~19mm 입니다.")
        elif value['fcstValue'] ==40:
            print("예상 강수량은 20~39mm 입니다.")
        elif value['fcstValue'] ==70:
            print("예상 강수량은 40~69mm 입니다.")
        elif value['fcstValue'] ==100:
            print("예상 강수량은 70mm이상 입니다.")
    else:
        pass




# RM1 = json_data["response"]["body"]["items"]["item"][5]["fcstValue"]
# print("예상 강수량은 " + str(RM1) + "mm 입니다.")
