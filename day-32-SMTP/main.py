import smtplib
import datetime as dt
import random

SMTP_PASSWORD = "os.environ['SMTP_PASS']"               #for gmail
MY_EMAIL = "os.environ['MAIN_EMAIL']"

#gmail server: smtp.gmail.com
#yahoo server: smtp.mail.yahoo.com

#connection = smtplib.SMTP("smtp.gmail.com", port=587)  #original way of doing it, can use the same trick as with file opening however:
# with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
#     connection.starttls()
#     connection.login(user=MY_EMAIL, password=SMTP_PASSWORD)
#     connection.sendmail(from_addr=MY_EMAIL,
#                         to_addrs="os.environ['TEST_MAIL']",
#                         msg="Subject: Test header\n\n Test body)

#connection.close() only necessary if using first method




# now = dt.datetime.now()             #gets very long string, but you can tap into singular attributes with .hour, .minute, etc
# hour = now.hour
# print(hour)

#date_of_birth = dt.datetime(year= 2002, month=6, day=7)
#print(date_of_birth)

with open("quotes.txt") as quotes:
    random_quote = random.choice(quotes.readlines())


current_date = dt.datetime.now()

if current_date.day == 5:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=SMTP_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs="os.environ['TEST_MAIL']",
                            msg=f"Subject: Motivational Monday\n\n {random_quote}")
