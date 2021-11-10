#-*- coding:utf-8 -*-
#Author:wangjian

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.header import Header
import smtplib
import time
import os,sys

class Smtp(object):
    '''
    send email
    '''
    def __init__(self,mail_server='smtp.qq.com'):
        self.mail_server = mail_server

    def find_report(self,dirpath):
        '''select new report'''
        lists = os.listdir(dirpath)
        lists.sort(key=lambda *fn:os.path.getmtime(os.path.join(dirpath,*fn)))
        new_report = lists.pop()
        return new_report

    def send_email(self,user,passwd,receive,reportdir,email_msg="测试报告附件已发送，请查收",email_title="自动化测试报告"):
        report_name = self.find_report(reportdir)
        reportpath = os.path.join(reportdir,report_name)
        with open(reportpath,'rb') as fp:
            mail_body = str(fp.read())
        msg = MIMEMultipart('alternative')
        body = MIMEText(eval(mail_body),'html','utf-8')
        body['Content-Type'] = 'application/octet-stream'
        body.add_header('Content-Disposition', 'attachment', filename=report_name)
        text_sub = MIMEText(email_msg, 'html', 'utf-8')
        msg.attach(text_sub)
        msg['Subject'] = Header(email_title,'utf-8')
        msg['from'] = Header(user,'utf-8')
        msg['to'] = Header(receive,'utf-8')
        msg.attach(body)
        try:
            smtp = smtplib.SMTP(self.mail_server,25)
        except:
            smtp = smtplib.SMTP_SSL(self.mail_server,465)
        try:
            smtp.login(user,passwd)
            smtp.sendmail(user,receive,msg.as_string())
            print("发送邮件成功")
        except Exception as e:
            print(f"发送邮件失败,失败原因：{e}")
        finally:
            smtp.quit()

if __name__ == '__main__':
    path = os.path.join(os.path.split(os.path.dirname(os.path.abspath(__file__)))[0],'report')
    sm = Smtp()
    sm.send_email('977653367@qq.com','nbbvzyyesggabcbb','3339496459@qq.com',path)
