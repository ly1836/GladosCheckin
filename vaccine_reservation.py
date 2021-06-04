import requests
import time
import json
import random

while(True):
    url = "https://xgsz.szcdc.net/crmobile/reservationStock/timeNumber?params=CXk3IOq9kjaX%2B%2Br9VGJGZBub7V0Ojc0a9wrDhj7IMvigWUafet9z3%2BMipziZ05kGidGSfsxbBGvgG1t3jjp4YF0gLudvKP6R6AX8hMWDzPvvsBMeedeGTR9mwquBMvv0"
    headers = {'selfappid': "wx5402a9708b90332e",
               "token": "-t-iRK8ohVw4Oy6Tlml1eo9pJ6mOl0TmMX6FIPvYAHCTy16Hq4qmMWRxdc4bx22GYWY",
               "ybm": "iWY1fJ4ireV+w1tgkQGolpeSU0vKkO9QtYKVO1/3LCA=",
               "appid": "app569d18f5",
               "otn": "h7B/vLFNZfmNOqq1AeH2Tcvp2nSmI3sAAMNNVvUXeY6V1Z8a8U3Tgr6K3O7zUGiO6Kk7KlA6ibArE4pE/uDcYkoe6flxzlcY+axLCpb+aaAGRLEiimzMoKmMYgHKBayN",
               "User-Agent": "Mozilla/5.0 (Linux; Android 6.0.1; Moto G (4)) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Mobile Safari/537.36"}
    response = requests.get(url, headers = headers)
    print(response.text)

    res = json.loads(response.text)
    code = int(res['ecode'])
    if(code == 1000):
        data = res['data']
        for d in data:
            restId = d['restId']
            depaId = d['depaId']
            ouatId = d['ouatId']
            # 总数
            restSum = d['restSum']
            # 日期
            restDate = d['restDate']
            # 剩余号数量
            restSurplus = d['restSurplus']
            # 开始时间
            ouatBeginTime = d['ouatBeginTime']
            # 结束时间
            ouatEndTime = d['ouatEndTime']

            print("发现日期[%s],接种时间为[%s-%s],剩余名额[%d]" % (restDate, ouatBeginTime, ouatEndTime, restSurplus))
            if(restSurplus > 0):
                print("==================================")
                print("已发现剩余名额，请抓紧时间填写验证码!!!")
                print("时间段为[%s-%s]" % (ouatBeginTime, ouatEndTime))
                print("==================================")
    else:
        print(res['msg'])

    s = random.uniform(1, 3)
    sleps = round(s, 2)
    time.sleep(sleps)
