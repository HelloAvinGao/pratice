from django.shortcuts import render
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

# Create your views here.
def indexPage(request):
    return render(request, 'index.html', {"titleName": "emailTest"})

def sendMail(request):
    try:
        if request.method == 'GET':
            # 第三方 SMTP 服务
            mail_host = "smtp.qq.com"  # 设置服务器
            mail_user = "1817932905@qq.com"  # 用户名
            mail_pass = "cawanyxmwtwyecbh"  # 口令 ：qq上是获得的客户端代码
            # 邮箱内容：邮箱地址、邮箱内容、发件人姓名、收件人姓名、邮箱标题
            receivers  = request.GET['receivers']
            content  = request.GET['emailContent']
            message = MIMEText(content, 'html', 'utf-8')
            message['From'] = formataddr(["菜鸟教程", mail_user])
            message['To'] = formataddr([receivers, receivers])
            message['Subject'] = "邮件标题"
            # 使用smtplib连接SMTP服务器，并发送邮件
            smtpObj = smtplib.SMTP()
            smtpObj.command_encoding = 'utf-8'
            smtpObj.connect(mail_host, 25)  # 25 为 SMTP 端口号
            smtpObj.login(mail_user, mail_pass)
            smtpObj.sendmail(mail_user, receivers, message.as_string())
            print('email successful')
    except Exception as e:
        print(e)
    return render(request, 'index.html', {"titleName": "emailTest"})


