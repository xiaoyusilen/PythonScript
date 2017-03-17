# coding:utf-8
# author by @xiaoyusilen

import smtplib
import ConfigParser
import email.Utils
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
def send_mail(to_list, cc_list, sub, text):

    conf = ConfigParser.ConfigParser()
    conf.read('config.conf')
    # 从配置文件中读取邮箱账号密码
    mailconfig = {
        'host': conf.get("mail", "mail_host"),
        'user': conf.get("mail", "mail_user"),
        'pass': conf.get("mail", "mail_pass"),
    }
    msg = MIMEText(text, _subtype='html', _charset='utf-8')
    msg['Subject'] = sub
    # send and cc list
    toAll = []
    if to_list[0]:
        # add send list
        msg['To'] = email.Utils.COMMASPACE.join(to_list)
        [toAll.append(i) for i in to_list]
    if cc_list[0]:
        # add cc list
        msg['Cc'] = email.Utils.COMMASPACE.join(cc_list)
        [toAll.append(i) for i in cc_list]
    try:
        send_smtp = smtplib.SMTP()
        send_smtp.connect(mailconfig['host'])
        send_smtp.login(mailconfig['user'], mailconfig['pass'])
        send_smtp.sendmail(mailconfig['user'], to_list, msg.as_string())
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

def combine_html(object):
    html = ""
    html = html + (HEADER)
    html = html + (object)
    html = html + (FOOTER)
    return html