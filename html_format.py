from smtplib import SMTP
host='smtp.gmail.com'
port='587'
username='aathena266@gmail.com'
password="#kafuuma2#"
from_email = username
to_list = ['aathena266@gmail.com']

email_conn =SMTP(host,port)
email_conn.ehlo()
email_conn.starttls()
email_conn.login(username, password)
email_conn.sendmail(username,to_list,'this is my first mail to you')
email_conn.quit()
