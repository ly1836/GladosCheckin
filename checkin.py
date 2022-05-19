# coding=utf-8
import requests
import argparse
import time
import json
import logging
import os
import sys

logging.basicConfig(format='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s',
                    level=logging.DEBUG)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--cookie", help='''
                                                请到【https://glados.rocks/console/checkin】页面拷贝cookie
                                                注意：一定要清除掉cookie值之间的空格，不然无法识别!!!
                                                ''')
    if parser is not None and parser.parse_args().cookie is not None:
        cookie = parser.parse_args().cookie

    else:
        env_dist = os.environ
        cookie = env_dist.get('cookie')

    if cookie is not None:
        cookie = str(cookie).replace(" ", "")
        logging.info("解析到的cookie:[%s]" % cookie)
    else:
        logging.info("未解析到cookie,请检查启动参数!")
        sys.exit(0)

    while True:
        if cookie is not None:
            headers = {'Cookie': str(cookie)}
            result = requests.post(url='https://glados.rocks/api/user/checkin', data={"token": "glados.network"},
                                   headers=headers).text
            nowTime = time.strftime('%Y-%m-%d %X', time.localtime())
            result_json = json.loads(result)
            # print("time:[%s]  ,response:[%s]" % (nowTime, result_json['message']))
            logging.info("time:[%s]  ,response:[%s]" % (nowTime, result_json['message']))
            # 休眠一天
            time.sleep(60 * 60 * 24)
        else:
            logging.info('''
                    请设置cookie运行,例如：
                    docker run -itd glados-checkin:1.0.0 --name my-glados-checkin -c='value'
                    请到【https://glados.rocks/console/checkin】页面拷贝cookie
                    注意：一定要清除掉cookie值之间的空格，不然无法识别!!!
                    ''')
            break
