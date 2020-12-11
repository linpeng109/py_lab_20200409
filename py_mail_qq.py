import smtplib
from email.mime.text import MIMEText


class QQMail:
    def __init__(self):
        self.email_user = '1911097168@qq.com'
        self.email_password = 'muerlqnrypihecif'
        self.email_smtp_host = 'smtp.qq.com'
        self.email_smtp_ssl_port = 465
        self.email_to = '1911097168@qq.com'
        self.email_from = '1911097168@qq.com'

    def send_mail(self):
        message = MIMEText('Test')
        message['Subject'] = 'Test'
        message['From'] = self.email_from
        message['To'] = self.email_to
        try:
            qqmail = smtplib.SMTP_SSL(host=self.email_smtp_host, port=self.email_smtp_ssl_port)
            qqmail.login(self.email_user, self.email_password)
            qqmail.sendmail(to_addrs=self.email_to, from_addr=self.email_from, msg=message.as_string())
            qqmail.quit()
        except smtplib.SMTPException as error:
            print('fail,%s' % error)



if __name__ == '__main__':
    qqmail = QQMail()
    qqmail.send_mail()
