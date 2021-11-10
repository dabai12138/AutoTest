#-*- coding:utf-8 -*-
#Author:wangjian

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.base import MIMEBase
from email.header import Header
from email.utils import parseaddr,formataddr
import smtplib
import time
import os,sys

PATH = lambda p:os.path.abspath(
    os.path.join(os.path.dirname(__file__),p)
)

def _format_addr(s):
    name,addr = parseaddr(s)
    return formataddr((Header(name,'utf-8').encode(),addr))

def send_mail(**kwargs):
    '''
    :param f:附件路径
    :param to_addr:发给的人 []
    :return:
    '''
    from_addr = kwargs["mail_user"]
    password = kwargs["mail_pass"]
    smtp_server = kwargs["mail_host"]

    msg = MIMEMultipart()
    msg['From'] = _format_addr('来自<%s>接口测试'%from_addr)
    msg['To'] = _format_addr('<%s>'%kwargs['to_addr'])
    msg['Subject'] = Header(kwargs['header_msg'],'utf-8').encode()
    msg.attach(MIMEText(kwargs['attach'],'plain','utf-8'))

    if kwargs.get('report','0') != 0:
        part = MIMEApplication(open(kwargs['report'],'rb').read())
        part.add_header('Content-Disposition','attachment',filename=('gb2312','',kwargs['report_name']))
        msg.attach(part)

    server = smtplib.SMTP_SSL(smtp_server,kwargs['port'])
    server.set_debuglevel(1)
    server.login(from_addr,password)
    server.sendmail(from_addr,kwargs['to_addr'],msg.as_string())
    server.quit()

class Smtp(object):
    '''
    send email
    '''
    def __init__(self,mail_server):
        self.mail_server = mail_server

    def find_report(self,dirpath):
        '''find new report'''
        lists = os.listdir(dirpath)
        lists.sort(key=lambda fn:os.path.getmtime(os.path.join(dirpath,fn)))
        new_report = lists.pop()
        return new_report

    def send_email(self,user,passwd,receive,reportdir):
        reportpath = os.path.join(reportdir,self.find_report(reportdir))
        with open(reportpath,'rb') as fp:
            mail_body = str(fp.read())
        msg = MIMEMultipart('alternative')
        body = MIMEText(eval(mail_body),'html','utf-8')
        body['Content-Type'] = 'application/octet-stream'
        body.add_header('Content-Disposition', 'attachment', filename='AutoTestReport.html')
        text_sub = MIMEText(u'测试报告附件：', 'html', 'utf-8')
        msg.attach(text_sub)
        msg['Subject'] = Header(u'自动化测试报告','utf-8')
        msg['from'] = Header(user,'utf-8')
        msg['to'] = Header(receive,'utf-8')
        msg.attach(body)
        try:
            smtp = smtplib.SMTP(self.mail_server,25)
        except:
            smtp = smtplib.SMTP_SSL(self.mail_server,465)
        smtp.login(user,passwd)
        smtp.sendmail(user,receive,msg.as_string())
        smtp.quit()



if __name__ == '__main__':
    # path = os.path.join(os.path.split(os.path.dirname(os.path.abspath(__file__)))[0],'report')
    # sm = Smtp('smtp.qq.com')
    # sm.send_email('977653367@qq.com','bpmwiayuonjzbbbb','3339496459@qq.com',path)


    to_addr = [""]
    mail_host = "smtp.qq.com"
    mail_user = ""
    mail_pass = ""
    port = "465"
    header_msg = "接口测试"
    attach = "接口测试"
    report = PATH("../logs/report.xlsx")
    send_mail(to_addr=to_addr,
              mail_host=mail_host,
              mail_user=mail_user,
              port=port,
              mail_pass=mail_pass,
              header_msg=header_msg,
              report=report,
              attach=attach,
              report_name='接口测试报告')