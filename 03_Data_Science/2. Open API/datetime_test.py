import urllib.request
import json
import datetime

#current time
now = datetime.datetime.now("%Y %m %d %I %M")
base_date=str(now.year)+str(now.month)+str(now.day)
base_time=str(now.hour)+str(now.minute)

print(now)
print(base_date)
print(base_time)

# location
x=89
y=91

# private key
service_key="Jvg5WLwXnf%2BbDrFmoNYHyoyudFYNVMBCwr375OfMUGIpwDuEIdM422XY%2BhVy60RhSeCKQXRFAVRauGlP%2B5xsYg%3D%3D&numOfRows=30"

url=f"http://newsky2.kma.go.kr/service/SecndSrtpdFrcstInfoService2/ForecastTimeData?base_date={base_date}&base_time={base_time}&nx={x}&ny={y}&_type=json&ServiceKey={service_key}"

print(url)