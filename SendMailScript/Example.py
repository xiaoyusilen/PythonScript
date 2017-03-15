# coding:utf-8
# author by @xiaoyusilen

import sys
import os
import smtplib
import pandas as pd
from utils.connect_mysql import MySQL

from email.mime.text import MIMEText
reload(sys)
sys.setdefaultencoding('utf-8')


# set css style
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

def send_query_data():

    # query some data from database
    db = MySQL()
    query_sql = "select * from test_table"
    db.query(query_sql)
    result = db.fetchOneRow()

    def convertToHtml(result,title):
        d = {}
        index = 0
        for t in title:
            d[t]=result[index]
            index = index+1
        df = pd.DataFrame(d)
        df = df[title]
        # use css style
        h = df.to_html(index=False,classes='table')
        return h

    if __name__ == '__main__':
        result = [result]
        title = [u'result']
        # save as Temporary Files
        with open('test.html', 'w') as f:
            f.write(HEADER)
            f.write(convertToHtml(result,title))
            f.write(FOOTER)

    # 定义发送列表
    file_object = open('test.html')
    try:
        all_the_text = file_object.read()
    finally:
        file_object.close()
        # delete Temporary Files
        os.remove('test.html')
    mailto_list = ["yourname@example.com"]
    # 邮件标题
    mail_title = 'test_mail'
    send_mail(mailto_list, mail_title, all_the_text)

    print "send successfully"

send_mail()