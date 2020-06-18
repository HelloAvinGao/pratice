from flask import Flask, jsonify,  current_app, request
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import base64

app = Flask(__name__)
CORS(app, supports_credentials=True)
CORS(app, resources=r'/*')

app.debug = True
app.config['SECRET_KEY'] = '123456'
def generate_token(api_users):
    expiration = 3600
    s = Serializer(current_app.config['SECRET_KEY'], expires_in=expiration) #expiration是过期时间
    try:
        token = s.dumps({"id": '1', "name": 'gao'}).decode("ascii")
        return token, expiration
    except Exception as e:
        app.logger.error("获取token失败:{}".format(e))

    return 'done'

@app.route('/find', methods=['GET','POST'])
def find():
    username = verify_token(request.args.get('token'))
    print(username)
    user = request.args.get('user')
    password = request.args.get('password')
    box_id = request.args.get('box_id')
    list = []
    token = generate_token(user)
    print('run here')
    str_token = str(token)
    list.append(str_token)
    print(list)
    json_data = jsonify(list)
    return json_data


def verify_token(token):
    '''
    校验token
    :param token:
    :return: 用户信息 or None
    '''

    # 参数为私有秘钥，跟上面方法的秘钥保持一致
    s = Serializer(current_app.config["SECRET_KEY"])
    try:
        # 转换为字典
        data = s.loads(token)
        return data
    except Exception:
        return None



if __name__ == '__main__':
    # app.debug = True
    app.run(host='127.0.0.1',port=5000)