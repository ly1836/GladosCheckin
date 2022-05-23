FROM quoinedev/python3.6-pandas-alpine:latest
MAINTAINER leiyang <leiyang753@gmail.com>

ADD ./ /code
WORKDIR /code

RUN pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

ENTRYPOINT python3 checkin.py $0 $@
