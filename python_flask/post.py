from flask import Flask,url_for,request,render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app, supports_credentials=True)
CORS(app, resources=r'/*')

app.debug = True
@app.route('/')
def hello_world():
    return "index.html + 1"

# @app.route('/login/<name>/<password>',methods=['POST'])
# def login(name,password):
#     if request.method == 'POST':
#         print(name + ' ' + password)
#         return (name + ' ' + password)
#     return 'login html'
#     # if request.method == 'POST':
#     #     return 'run here'
#     #     # if request.form['user'] == 'admin':
#     #     #     return 'Admin login successfully!'
#     #     # else:
#     #     #     return 'No such user!'
#     # return "login html"
@app.route('/login',methods=['POST'])
def login():
    password = request.values.get('password').strip()
    name = request.values.get('userName').strip()
    print(name + ' ' + password)
    if request.method == 'POST':
        return {"token":"helloworld","userInfo":{"id":"id"}}
    return 'login html'



if __name__ == '__main__':
    # app.debug = True
    app.run(host='127.0.0.1',port=5000)