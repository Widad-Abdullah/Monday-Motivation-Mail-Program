import smtplib
import random
import datetime as dt

# Your Email to send from
EMAIL=""
# Your Email's app password
PASSWORD=""
# Receivers Email
TO_EMAIL=""

now = dt.datetime.now()

if now.weekday()==0:
    with open("quotes.txt") as q:
        quotes_list=q.readlines()
        quote=random.choice(quotes_list)
    print(quote)
    with smtplib.SMTP("smtp.gmail.com",port=587) as connection:
        connection.starttls()
        connection.login(user=EMAIL,password=PASSWORD)
        connection.sendmail(from_addr=EMAIL,
                            to_addrs=TO_EMAIL,
                            msg=f"Subject:Monday Motivation\n\n{quote}")
