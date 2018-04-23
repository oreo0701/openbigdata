import json


with open("이명박_naver_news.json", encoding='utf-8') as json_data:
    json_data_load = json.load(json_data)
    json_data_string = json.dumps(json_data_load)
    jsonResult = json.loads(json_data_string)

print("데이터 분석을 시작합니다..")

for line in jsonResult:
    if line.get('org_link') == None:
        print(line)
    else:
