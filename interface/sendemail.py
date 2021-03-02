import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
from email.header import Header
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart

import os, sys
from nt import chdir             #判断目录是否存在并切换目录

print("正在发送...")
#登陆邮件服务器
smtpObj=smtplib.SMTP('smtp.qq.com', 587)
smtpObj.ehlo()
smtpObj.starttls()
#传入相应的账号密码信息
smtpObj.login('1021295302@qq.com', 'vgnjpnaeuwaqbbbi')

#邮件收发信人信息
sender = '1021295302@qq.com'#发件人信息
receivers = ['2431320433@qq.com']#收件人信息

#完善发件人收件人，主题信息
message = MIMEMultipart()
message['From'] = formataddr(["姚佳龙", sender])
message['To'] = formataddr(["wqx", ''.join(receivers)])
subject = '测试报告'
message['Subject'] = Header(subject, 'utf-8')

#正文部分
textmessage = MIMEText('', 'html', 'utf-8')
message.attach(textmessage)

workLoc = os.path.join('E:\\', 'pythonProject', 'interface')
# #检查路径有效性
if (os.path.exists(workLoc)) & (os.path.isdir(workLoc)):
#尝试改变当前工作路径：
    chdir(workLoc)
else:
    print('路径无效，请从新检查')
    sys.exit()

#尝试添加附件
File = '报告.html'
print("附件文件名为：%s" %File)
FileLoc = os.path.join(workLoc, File)
FileAtt = MIMEApplication(open(FileLoc, 'rb').read())
FileAtt.add_header('Content-Disposition', 'attachment', filename=File)
message.attach(FileAtt)

#发送邮件操作
smtpObj.sendmail(sender, receivers, message.as_string())
smtpObj.quit()
print("发送成功！")