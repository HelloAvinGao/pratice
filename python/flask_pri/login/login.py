from flask import Flask,session,render_template,request,redirect,url_for
from datetime import timedelta  #导入过期时间库
import json,os

app=Flask(__name__)

app.config ['SECRET_KEY'] = os.urandom(24) #每一次服务器启动后，SECRET_KEY(盐)不一样
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=7)  #配置过期时间

account = {
    "admin":"admin"
}

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method=='POST':
        if request.form['username'] == account['admin']:
            session['username']=request.form['username']
            session['password']=request.form['password']
            session.permanent = True
            return redirect(url_for('index'))
        else:
            return render_template('./template/login.html')

@app.route('/logout')
def logout():
    # session.pop('username',None)
    print(session.get('username'))
    session.pop('username') #删除session
    print(session.get('username'))
    # return 'pop success'
    return redirect(url_for('login'))

@app.route('/')
def index():
    login=False
    if 'username' in session:
        login=True
    return render_template('index.html',login=login)

# 用于测试
@app.route("/api",methods = ['GET','POST'])
def API():
    data = {
        "username": "user.username",
        "theme": "user.theme",
        "image": "a",
    }

    if request.method=='GET':
        return data
    if request.method=='POST':
        array = json.loads(request.data)
        for key in array:
            data[key] = array[key]
        return data
    

if __name__=='__main__':
    app.run(debug=True)