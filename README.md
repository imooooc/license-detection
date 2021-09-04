# license-detection

#### 介绍
{**基于视频的车牌识别系统**
本系统是一个基于人工智能算法的车牌识别系统，用户通过使用由我们团队开发的微信小程序上传媒体文件（视频/图片），该文件会在我们强大的算法系统后台进行基于人工智能算法进行计算和识别，从而得出车牌号等信息，然后将数据返回给客户端。同时用户也可以通过输入车牌号来寻找我们数据库中所拥有的车辆信息。}

#### 软件架构
我们采用C/S的前后端分离的软件架构，目前客户端选择开发一个简单便捷易上手的微信小程序，服务器端则使用Python Web主流框架Django打造一个包含后端管理系统在内的强大而完善的后台服务系统，足以满足业务需求，同时具备扩展性。

#### 使用说明

1.  用户无需主动安装app，只需要打开微信搜索微信小程序“微吉珠”即可
2.  或者扫描小程序二维码
3.  管理人员可以通过https://vmoli.com/admin登陆后端管理系统
4.  官网首页：https://vmoli.com

#### API


###### 用户

获取用户列表

- 请求地址

```
GET https://vmoli.com/u/users
```

- 请求参数

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| ---- | ---- | ------ | ---- | ---- |
| -    | -    | -      | -    | -    |

- 返回值

Object

返回的JSON数据包

| 属性        | 类型   | 说明       |
| ----------- | ------ | ---------- |
| id          | int    | 用户的id   |
| openid      | string | 用户openid |
| stu_id      | string | 用户的学号 |
| pwd         | string | 用户密码   |
| name        | string | 用户姓名   |
| create_time | string | 创建时间   |

- 请求示例

```http
GET /u/users HTTP/1.1
Host: vmoli.com
```

- 返回数据示例

```json
[
    {
        "id": 1,
        "openid": "001",
        "stu_id": "04170413",
        "pwd": "123123",
        "name": "小拾",
        "create_time": "2020-04-07T19:42:47.104934+08:00"
    },
    {
        "id": 2,
        "openid": "002",
        "stu_id": "04170415",
        "pwd": "123123",
        "name": "白蛋",
        "create_time": "2020-04-07T19:43:04.079454+08:00"
    }
]
```

---
创建新用户

- 请求地址
```
POST https://vmoli.com/u/users
```

- 请求参数

| 属性   | 类型   | 默认值 | 必填 | 说明       |
| ------ | ------ | ------ | ---- | ---------- |
| openid | string | -      | 是   | 必填且唯一 |
| stu_id | string | 空     | 否   | -          |
| pwd    | string | 空     | 否   | -          |
| name   | string | nobody | 否   | -          |


- 返回值

Object

返回的JSON数据包

| 属性        | 类型   | 说明         |
| ----------- | ------ | ------------ |
| id          | int    | 新增用户的id |
| openid      | string | -            |
| stu_id      | string | -            |
| pwd         | string | -            |
| name        | string | -            |
| create_time | string | 创建时间     |


- 请求示例
```http
POST /u/users HTTP/1.1
Host: vmoli.com

Content-Disposition: form-data; name="openid"

000

Content-Disposition: form-data; name="stu_id"

041734534

Content-Disposition: form-data; name="pwd"

123123145

Content-Disposition: form-data; name="name"

司马光


```


- 返回数据示例

```json
{
    "id": 7,
    "openid": "000",
    "stu_id": "041734534",
    "pwd": "123123145",
    "name": "司马光",
    "create_time": "2020-04-11T22:38:42.109987+08:00"
}
```

---

###### 用户操作
用户查询历史
- 请求地址

```
GET https://vmoli.com/o/history
```

- 请求参数

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| ---- | ---- | ------ | ---- | ---- |
| -    | -    | -      | -    | -    |

- 返回值

Object

返回的JSON数据包

| 属性     | 类型   | 说明           |
| -------- | ------ | -------------- |
| id       | int    | 记录id         |
| plate    | strng  | 车牌号         |
| add_time | string | 添加时间       |
| user     | int    | 查询用户的id号 |

- 请求示例

```http
GET /o/history HTTP/1.1
Host: vmoli.com
```

- 返回数据示例

```json
[
    {
        "id": 1,
        "plate": "苏XXXXXXX",
        "add_time": "2020-04-07T19:48:39.072727+08:00",
        "user": 2
    }
]
```

---

新增查询历史
- 请求地址

```
POST http://vmoli.com/o/history
```

- 请求参数

| 属性  | 类型  | 默认值 | 必填 | 说明               |
| ----- | ----- | ------ | ---- | ------------------ |
| plate | sting | 空     | 否   | 用户输入的查询信息 |
| user  | int   | -      | 是   | 请求查询的用户id   |

- 返回值

Object

返回的JSON数据包

| 属性     | 类型   | 说明             |
| -------- | ------ | ---------------- |
| id       | int    | 记录id值         |
| plate    | string | 查询信息         |
| add_time | string | 查询时间         |
| user     | int    | 请求查询的用户id |


- 请求示例

```http
POST /o/history/ HTTP/1.1
Host: 
Content-Type: multipart/form-data; 

Content-Disposition: form-data; name="plate"

浙b98703

Content-Disposition: form-data; name="user"

1


```

- 返回数据示例

```json
{
    "id": 2,
    "plate": "浙b98703",
    "add_time": "2020-04-11T22:56:47.341279+08:00",
    "user": 1
}
```

---

车牌找图
- 请求地址

```
GET http://vmoli.com/o/search
```

- 请求参数

| 属性 | 类型   | 默认值 | 必填 | 说明           |
| ---- | ------ | ------ | ---- | -------------- |
| q    | string | 空     | 是   | 要查询的车牌号 |

- 返回值

Object

返回的JSON数据包

| 属性        | 类型   | 说明           |
| ----------- | ------ | -------------- |
| id          | int    | 该图片的id号   |
| source      | string | 图片的路由地址 |
| desc        | string | 额外信息       |
| create_time | string | 上传时间       |
| user        | int    | 上传用户的id   |
| car         | int    | 对应车辆的id   |

- 请求示例

```http
GET /o/search?q=川QK9777 HTTP/1.1
Host: vmoli.com
Content-Type: multipart/form-data; 
```

- 返回数据示例

```json
[
    {
        "id": 13,
        "source": "/media/images/2020/04/wx6afc66b1b9773c81.o6zAJs7tN9g8fp1OMo8Rs03Lq1TE.KcBu6E7dXTU95ed868940d566332f4ab168f22a12d51.jpg",
        "desc": "一张没有描述的图片",
        "create_time": "2020-04-08T21:34:53.131635+08:00",
        "user": 1,
        "car": 3
    },
    {
        "id": 18,
        "source": "/media/images/2020/04/wx6afc66b1b9773c81.o6zAJs7tN9g8fp1OMo8Rs03Lq1TE.kz5j2CE9My2r5ed868940d566332f4ab168f22a12d51.jpg",
        "desc": "一张没有描述的图片",
        "create_time": "2020-04-08T22:23:39.950161+08:00",
        "user": 1,
        "car": 3
    },
```

---
#### 参与贡献

1.  Fork 本仓库
2.  新建 Feat_xxx 分支
3.  提交代码
4.  新建 Pull Request



