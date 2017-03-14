# coding:utf-8
# author by @xiaoyusilen

import sys
import smtplib

from email.mime.text import MIMEText
reload(sys)
sys.setdefaultencoding('utf-8')

# 发送邮件函数
def send_mail(to_list, sub, text):

    # 设置服务器名称、用户名、密码以及邮件后缀
    mail_host = "xxxxx"
    mail_user = "yourname@example.com"
    mail_pass = "******"
    msg = MIMEText(text, _subtype='html', _charset='utf-8')
    msg['Subject'] = sub
    msg['From'] = 'yourname@example.com'
    msg['To'] = ";".join(to_list)
    try:
        send_smtp = smtplib.SMTP()
        send_smtp.connect(mail_host)
        send_smtp.login(mail_user, mail_pass)
        send_smtp.sendmail('yourname@example.com', to_list, msg.as_string())
        send_smtp.close()
        return True
    except Exception, e:
        print str(e)
        return False

# write something to mail
text = "test"

# 定义发送列表
mail_text = text
mailto_list = ["yourname@example.com"]
send_mail(mailto_list, 'test', mail_text)

print "success"