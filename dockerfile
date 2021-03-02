FROM my-python:3.6.0
MAINTAINER leiyang <leiyang@qq.com>

ADD ./GladosCheckin /code
WORKDIR /code

RUN pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

ENTRYPOINT python3 checkin.py $0 $@
