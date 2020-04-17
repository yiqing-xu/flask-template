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
    - python manage.py runserver -h 0.0.0.0 -p 8000 -r -d
- 生产
    - gunicorn manage:app -b 0.0.0.0:8000 -w 4
