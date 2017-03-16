# coding:utf-8
# author by @xiaoyusilen

import sys

from utils.connect_mysql import MySQL
from base_mail import send_mail,HEADER,FOOTER,convertToHtml

reload(sys)
sys.setdefaultencoding('utf-8')

def send_query_data():

    # query some data from database
    db = MySQL()
    query_sql = "select * from test_table"
    db.query(query_sql)
    result = db.fetchOneRow()

    if __name__ == '__main__':
        result = [result]
        title = ['Title']
        html = ""
        html = html + (HEADER)
        html = html + (convertToHtml(result,title))
        html = html + (FOOTER)

    # 定义发送列表
    mailto_list = ["yourname@example.com"]
    # 邮件标题
    mail_title = 'test_mail'
    send_mail(mailto_list, mail_title, html)

    print "send successfully"

send_mail()