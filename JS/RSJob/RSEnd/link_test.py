from flask import Flask, json, request, jsonify
from flask_cors import CORS
import pymysql
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
CORS(app, resource={r'/*': {'origins': '*'}})

# #添加用户节点
@app.route('/adduser', methods=['get', ])
def adduser():
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='root', charset='utf8')
    cursor = conn.cursor()
    conn.commit()
    cursor.execute('use gpaper')
    datalist = []
    datalist.append(request.form.get("account"))
    datalist.append(request.form.get("password"))
    print(datalist)
    # 进入数据库bdjs
    # 向newscontent添加数据
    sql = "SELECT * FROM `userinfo` WHERE `account`= '" + str(datalist[0]) + "';"
    res1 = cursor.execute(sql)
    if res1 == 1:
        return "no"
    sql2 = "INSERT INTO `userinfo`(`account`, `password`) VALUES('" + str(datalist[0]) + "','" + str(
        datalist[1]) + "');"
    res = cursor.execute(sql2)
    conn.commit()
    cursor.close()
    conn.close()
    return "ok"


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000, debug=True)