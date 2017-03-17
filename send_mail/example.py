# coding:utf-8
# author by @xiaoyusilen

import sys

from utils.connect_mysql import MySQL
from base_mail import send_mail,convertToHtml,combine_html

reload(sys)
sys.setdefaultencoding('utf-8')

def send_query_data():

    # query some data from database
    db = MySQL()
    query_sql = "select * from test_table"
    db.query(query_sql)
    result = db.fetchOneRow()

    # query_result
    result = [result]
    title = ['Title']
    html = combine_html(convertToHtml(result,title))

    # send_list
    mailto_list = ["yourname@example.com"]
    cc_list = ["yourname@example", "someother@example.com"]

    # maile_title
    mail_title = 'test_mail'
    send_mail(mailto_list, cc_list, mail_title, html)

    print "send successfully"

send_mail()