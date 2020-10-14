# coding=utf-8
import os
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from com.log import MyLog as Log
from com.readConfig import ReadBaseConfig
from com import readConfig


pro_dir = readConfig.pro_dir
log = Log(basedir=pro_dir, name="email.log")
rbc = ReadBaseConfig()
mail_host = rbc.get_mail_config(name="mail_host")
mail_port = rbc.get_mail_config(name="mail_port")
smtp_server = rbc.get_mail_config("mail_server")
mail_user = rbc.get_mail_config(name="mail_user")
mail_passwd = rbc.get_mail_config(name="mail_password")
mail_sender = rbc.get_mail_config(name="mail_sender")
mail_receivers = rbc.get_mail_config(name="mail_receiver")
print(mail_receivers)
mail_subject = rbc.get_mail_config(name="mail_subject")


class MyEmail(object):
    def __init__(self, server=smtp_server, user=mail_user, passwd=mail_passwd, sender=mail_sender,
                 receivers=mail_receivers, subject=mail_subject, host=mail_host, port=mail_port):
        self.host = host
        self.port = port
        self.smtpserver = server
        self.user = user
        self.password = passwd
        self.sender = sender
        self.receivers = receivers.split(',')
        self.subject = subject

    def send_email(self, mail_body):
        mail_body = "(本邮件是程序自动下发的，请勿回复！)\r\n" + mail_body
        msg = MIMEText(mail_body, 'html', 'utf-8')
        msg['Subject'] = Header(self.subject, 'utf-8')
        msg['From'] = Header(self.user, 'utf-8')
        # print("list %s" %list(self.receivers))
        for receiver in self.receivers:
            msg['To'] = Header(receiver, 'utf-8')

        try:
            smtp = smtplib.SMTP()
            # smtp = smtplib.SMTP_SSL()  # linux上使用smtp发送邮件需要使用SMTP_SSL
            smtp.connect(self.smtpserver, self.port)
            log.info("link to email sever success")
            smtp.login(self.user, self.password)
            log.info("login smtp server success")
            smtp.sendmail(self.sender, self.receivers, msg.as_string())
            log.info("send email success!")

        except Exception as e:
            log.error("发送邮件异常")
            log.error(e)
        finally:
            try:
                smtp.quit()
            except Exception as e:
                log.error("关闭smtp异常: %s" %e)
                # mylog.error(e)


if __name__ == "__main__":
    email = MyEmail()
    email.send_email("test test")
