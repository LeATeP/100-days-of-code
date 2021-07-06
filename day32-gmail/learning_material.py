import smtplib as sm
import datetime as dt
import pandas as pd
import random

my_email = "email address"
my_password = "email password"

data = pd.read_csv("quotes.txt", sep=" ", header=None)

rand_num = random.randint(0, 100)
quote = data.iloc[rand_num][0]


if dt.datetime.now().weekday() == 0:
    with sm.SMTP("smtp.gmail.com") as pipe:
        pipe.starttls()
        pipe.login(user=my_email, password=my_password)

        pipe.sendmail(from_addr=my_email, to_addrs="leateps@gmail.com", msg=f"Subject:Quote of the day\n\n{quote}")

# another solution
# with open("quotes.txt") as file:
#   all_quotes = file.readlines()
#   quote = random.choice(all_quotes)
