import smtplib

smtpObj= smtplib.SMTP('smtp.gmail.com',587)#smtp.office365.com  smtp.mail.yahoo.com

smtpObj.ehlo()

smtpObj.starttls()
smtpObj.login('yourEMailadress','yourPassword')

smtpObj.sendmail('senderEmail','recipientEmail',
'Subject: bla\n\n hello from Linux')

smtpObj.quit()