import smtplib, os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication


def send_notification(target_file_path, filename):

  smtp_server = 'smtp.163.com'
  smtp_port = 25
  smtp_username = 'kqx0731@163.com'
  smtp_password = os.environ['smtp_password']

  from_email = 'kqx0731@163.com'
  to_email = 'kqx0731@gmail.com,1025598017@qq.com'
  subject = 'Hello, world!'

  # 如名字所示Multipart就是分多个部分
  msg = MIMEMultipart()
  msg["Subject"] = subject
  msg["From"] = from_email
  msg["To"] = to_email

  # ---这是文字部分---
  part = MIMEText("我是邮件内容")
  msg.attach(part)

  # ---这是附件部分---
  tmp_file = os.path.join(target_file_path, filename)
  # print(tmp_file)
  part = MIMEApplication(open(tmp_file, 'rb').read())
  part.add_header('Content-Disposition', 'attachment', filename=filename)
  msg.attach(part)

  s = smtplib.SMTP(smtp_server, smtp_port)  # 连接smtp邮件服,这里是网易邮箱 务器,端口默认是25
  s.login(smtp_username, smtp_password)  # 登陆服务器
  s.sendmail(from_email, to_email, msg.as_string())  # 发送邮件
  s.close()

  #节省服务器空间！！
  # for file in os.listdir(target_file_path):
  #     os.remove(os.path.join(target_file_path,file))
  # os.rmdir(target_file_path)
