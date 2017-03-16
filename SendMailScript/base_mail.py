# coding:utf-8
# author by @xiaoyusilen

import smtplib
import pandas as pd
from email.mime.text import MIMEText

HEADER = '''
    <style type="text/css">
        body,table{
            font-size:12px;
            float: left;
        }
        table{
            table-layout:fixed;
            empty-cells:show;
            border-collapse: collapse;
            margin:0 auto;
            float: left;
        }
        td{
            height:30px;
        }
        .table{
            border:1px solid #cad9ea;
            color:#666;
            float: left;
        }
        .table th {
            background-repeat:repeat-x;
            height:30px;
            text-align: center;
        }
        .table td,.table th{
            border:1px solid #cad9ea;
            padding:0 1em 0;
        }
        .table tr.alter{
            background-color:#f5fafe;
        }
    </style>
    <body>
'''
FOOTER = '''
    </body>
</html>
'''

# 发送邮件函数
def send_mail(to_list, sub, text):

    # 设置服务器名称、用户名、密码以及邮件后缀
    mail_host = "smtp.letv.cn"
    mail_user = "LeShare_info@le.com"
    mail_pass = "arH05#jgvjvT"
    msg = MIMEText(text, _subtype='html', _charset='utf-8')
    msg['Subject'] = sub
    msg['From'] = 'LeShare_info@le.com'
    msg['To'] = ";".join(to_list)
    try:
        send_smtp = smtplib.SMTP()
        send_smtp.connect(mail_host)
        send_smtp.login(mail_user, mail_pass)
        send_smtp.sendmail('LeShare_info@le.com', to_list, msg.as_string())
        send_smtp.close()
        return True
    except Exception, e:
        print str(e)
        return False

def convertToHtml(result,title):
    d = {}
    index = 0
    for t in title:
        d[t]=result[index]
        index = index+1
    df = pd.DataFrame(d)
    df = df[title]
    h = df.to_html(index=False,classes='table')
    return h