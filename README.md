# 项目说明

### 使用flask_restful构建restful风格api

### 概要
- 用户模块
    - 使用flask_login和flask_session配合完成用户登录验证
- swagger
    - 使用flask模板语言建立swagger文档渲染
- socketio
    - 建立全双工socket通信链接

### 目录结构
```
│  .gitignore
│  manage.py                基于flask_script脚本启动
│  README.md                说明
│  requirements.txt         依赖库
├─app                       create_app
│  │  apis.py               flask—restful Resource资源
│  ├─socketio               socket服务
│  │      apis.py
│  ├─swagger                接口文档
│  │  │  apis.py
│  │  │  routes.py
│  ├─users                  用户
│  │  │  apis.py
│  │  │  models.py
│  │  │  routes.py
├─backend
│  │  conf.cfg              数据库配置文件
│  │  config.py             app.from_object()
│  ├─dbs                    数据库实例
│  │  │  mysql.py
│  ├─utils                  工具
│  │  │  snowflake.py
├─scripts                   脚本
├─static
│  └─swagger
│      └─docs               接口文档yaml文件
│              backend.yaml
│              swagger.yaml
└─templates
```
启动服务器：
- 开发
    - python manage.py runserver -h 0.0.0.0 -p 8000 -r -d  启动wsgi服务
    - python manage.py socketserver -h 0.0.0.0 -p 6888     启动socketio服务(内带wsgi)
- 生产
    以uwsgi单进程，多端口的方式启动多个进程(gunicorn不支持sticky sessions)
    uwsig --http :6888 --eventlet 1000 --http-websockets --master --wsgi-file manage.py --callable app
```
使用nginx的负载均衡，
负载均衡器必须配置为将来自给定客户端的所有HTTP请求始终转发给同一个worker，
使用ip_hash指令将路由为 /socketio/ 的请求转发到同一个端口即可
Flask-SocketIO支持负载均衡器后面的多个workers。
部署多个workers使得使用Flask-SocketIO的应用程序能够在多个进程和主机之间传播客户端连接，
并以这种方式进行扩展以支持大量的并发客户端。
```
```
nginx.conf

upstream socketio_nodes {
    ip_hash;
    server 127.0.0.1:8000;
    server 127.0.0.1:8001;
    server 127.0.0.1:8002;
    server 127.0.0.1:8003;
    # to scale the app, just add more nodes here!
}
server {
    listen 80;
    server_name dispatch-sandbox.iqusong.com;
    access_log /var/log/nginx/access_log main;
    error_log /var/log/nginx/error_log info;
    location /api {
        proxy_pass http://socketio_nodes;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
     }
    location /socket.io{
        proxy_pass http://socketio_nodes/socket.io;
        proxy_http_version 1.1;
        proxy_redirect off;
        proxy_buffering off;
        proxy_set_header Host $host;
        proxy_set_header X-Real-UP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "Upgrade";
     }
}
```