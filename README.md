### Glados自动签到


## 使用docker镜像

运行命令：
<b> docker run -itd --name my-glados-checkin ly753/glados-checkin:1.0.0 -c='cookie'  </b>

1. -itd：后台运行，要查看日志请用docker logs命令。
2. --name：后面跟容器名字。
3. ly753/glados-checkin:1.0.0：镜像名字
4. -c='cookie'：到 https://glados.rocks/console/checkin 页面随便找一个接口，查看 request header 中的 Cooike ，整个拷贝下来，然后<b>去除cookie中间的空格</b>，替换到示例中的cookie，运行即可。

例如：
```shell
docker run -itd --name my-glados-checkin ly753/glados-checkin:1.0.0 -c='cookie:xxx'
```

## 项目生成requirements.txt
#### 安装
```shell
pip install pipreqs
```

#### 在当前目录生成
```shell
pipreqs . --encoding=utf8 --force
```

## 安装依赖
```shell
pip install -r requirements.txt
```