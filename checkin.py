import sys
import requests
import argparse
import time


if __name__ =='__main__':
    print("argv:[%s]" % str(sys.argv))
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--cookie", help='''
                                                请到【https://glados.rocks/console/checkin】页面拷贝cookie
                                                注意：一定要清除掉cookie值之间的空格，不然无法识别!!!
                                                ''')
    cookie = parser.parse_args().cookie
    if(cookie != None):
        print("解析到的Cookie:[%s]" % cookie)

    while True:

        if(cookie != None):
            headers = {'Cookie': str(cookie)}
            result = requests.post(url='https://glados.rocks/api/user/checkin', data={"token": "glados_network"},
                                   headers=headers).text
            nowTime = time.strftime('%Y-%m-%d %X', time.localtime())
            print("time:[%s]  ,response:[%s]" % (nowTime, result))
            # 休眠一天
            time.sleep(60 * 60 * 24)
        else:
            print('''
                    请设置cookie运行,例如：
                    docker run -itd glados-checkin:0.0.1 --name my-glados-checkin -c='value'
                    请到【https://glados.rocks/console/checkin】页面拷贝cookie
                    注意：一定要清除掉cookie值之间的空格，不然无法识别!!!
                    ''')
            break

