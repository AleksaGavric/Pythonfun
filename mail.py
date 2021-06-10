import smtplib

conn = smtplib.SMTP("smtp.gmail.com", 587)
conn.ehlo()
conn.starttls()
conn.login("your email", "password")


def send_mail_to(to, subject, what, how_many):
    mail_contents = "%s\n\n\n%s" % (subject, what)
    print(mail_contents)
    if type(to) == list:
        for x in range(1, how_many):
            conn.sendmail("", ", ".join(to), mail_contents)
    else:
        for x in range(1, how_many):
            conn.sendmail("", to, mail_contents)


send_mail_to("TO", "SUBJECT", "body", 10)

conn.quit()
