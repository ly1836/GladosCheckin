# coding=utf-8
import requests
import argparse
import time
import json
import logging
import os
import sys
import random

logging.basicConfig(format='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s',
                    level=logging.DEBUG)

proxies = {}
cookies = set()

'''
    读取配置
'''
def read_configuration():
    global proxies
    global cookies
    http_proxy = None
    https_proxy = None

    # step1.优先获取环境变量
    env_dist = os.environ
    # step1.获取系统环境变量中的
    try:
        for key in env_dist.keys():
            if "http_proxy" in key:
                http_proxy = env_dist.get(key)

            if "https_proxy" in key:
                https_proxy = env_dist.get(key)

            if "cookie_" in key:
                if env_dist.get(key) is not None:
                    cookies.add(str(cookie))

    except Exception as e:
        print(e)

    # step2.获取指定路径下json文件【/config/cookies.json】
    try:
        with open("/config/cookies.json", 'r') as load_f:
            load_dict = json.load(load_f)
            print(load_dict)

            # 代理
            http_proxy = load_dict.get('http_proxy', "")
            https_proxy = load_dict.get('https_proxy', "")

            for c in load_dict['cookies']:
                cookies.add(str(c['cookie']))
    except Exception as e:
        print(e)

    # step3.获取命令行的
    if len(cookies) == 0:
        # 获取命令行参数
        parser = argparse.ArgumentParser()
        parser.add_argument("-c", "--cookie", help='''
                                                                请到【https://glados.rocks/console/checkin】页面拷贝cookie
                                                                注意：一定要清除掉cookie值之间的空格，不然无法识别!!!
                                                                ''')
        parser.add_argument("-http_proxy", "--http_proxy", help='http代理')
        parser.add_argument("-https_proxy", "--https_proxy", help='https代理')
        http_proxy = parser.parse_args().http_proxy
        https_proxy = parser.parse_args().https_proxy
        cookies.add(parser.parse_args().cookie)

    if http_proxy is not None:
        proxies['http'] = str(http_proxy)
    if http_proxy is not None:
        proxies['https'] = str(https_proxy)


if __name__ == '__main__':
    read_configuration()

    try:
        logging.info("代理：%s" % str(proxies))
        if cookies is not None:
            for cookie in cookies:
                cookie = str(cookie).replace(" ", "")
                logging.info("解析到的cookie:[%s]" % cookie)
        else:
            logging.info("未解析到cookie,请检查启动参数!")
            sys.exit(0)

        error_count = 0
        while True:
            if len(cookies):
                try:
                    for cookie in cookies:
                        headers = {'Cookie': str(cookie)}

                        result = requests.post(url='https://glados.rocks/api/user/checkin',
                                               data={"token": "glados.network"},
                                               headers=headers,
                                               proxies=proxies).text
                        nowTime = time.strftime('%Y-%m-%d %X', time.localtime())
                        result_json = json.loads(result)
                        # print("time:[%s]  ,response:[%s]" % (nowTime, result_json['message']))
                        logging.info("time:[%s]  ,response:[%s]" % (nowTime, result_json['message']))
                        time.sleep(1)
                    # 休眠一天
                    time.sleep(60 * 60 * 24)
                    # 再随机睡眠
                    randint = random.randint(0, 60)
                    time.sleep(randint)
                except Exception as ex:
                    logging.error("程序出现异常!" + str(ex))
                    logging.error("请到【https://glados.rocks/console/checkin】页面拷贝cookie,注意：一定要清除掉cookie值之间的空格，不然无法识别!!!")
                    time.sleep(60)
                    error_count = error_count + 1
                    if error_count > 10:
                        sys.exit(0)
            else:
                logging.info('''
                        请设置cookie运行,例如：
                        docker run -itd glados-checkin:1.0.0 --name my-glados-checkin -c='value'
                        请到【https://glados.rocks/console/checkin】页面拷贝cookie
                        注意：一定要清除掉cookie值之间的空格，不然无法识别!!!
                        ''')
                break
    except BaseException as ex:
        logging.error("程序异常!")
        logging.error(ex)
