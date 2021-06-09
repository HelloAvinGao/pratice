# -*- coding:utf-8 -*-

from flask import Flask, render_template

# 这里在浏览器中可以直接访问到static文件夹中的的静态文件．
# 例如要获取01.html,则直接输入　127.0.0.1:8866/static/01.html  即可．
# 在Flask的参数中可以设置:
# 1,静态文件夹的路径（模板文亦是如此），　static_folder = 自定义的文件夹（默认是static）,
# 2,静态文件夹的访问路径（模板文亦是如此），　static_url_path = 自定义的访问路径（默认的是/）
app = Flask(__name__)


# 直接获取templates文件夹中的的静态html模板
@app.route('/just_get')
def just_get():
    return render_template('show_image.html')


@app.route('/')
def test():
    return "hello world!!!"

if __name__ == '__main__':
    # 调试模式的作用：
    # １，离开pycharm，程序自动重新运行，
    # ２，在浏览其中可以查看错误信息
    # 参数１，开启调试模式，２，指定端口号
    app.run(debug=True, port=8866)