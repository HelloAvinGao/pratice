#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
 
# 第三方 SMTP 服务
mail_host="smtp.qq.com"  #设置服务器
mail_user="1817932905@qq.com"    #用户名
mail_pass="cawanyxmwtwyecbh"   #口令 
 
 
sender = '1817932905@qq.com'
receivers = '1835705783@qq.com'  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
 
message = MIMEText('Python 邮件发送测试...', 'plain', 'utf-8')
message['From'] = formataddr(["菜鸟教程",sender])
message['To'] = formataddr([receivers,receivers])
 
message['Subject']="菜鸟教程发送邮件测试"
 
 
try:
    smtpObj = smtplib.SMTP()
    smtpObj.command_encoding = 'utf-8'
    smtpObj.connect(mail_host, 25)    # 25 为 SMTP 端口号
    smtpObj.login(mail_user,mail_pass)  
    smtpObj.sendmail(sender, receivers, message.as_string())
    print("邮件发送成功")
except smtplib.SMTPException:
    prin("Error: 无法发送邮件")