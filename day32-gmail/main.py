import datetime as dt, pandas as pd
import smtplib as sm
import random

# 1. Update the birthdays.csv
my_email = "email address"
my_password = "email password"

# 2. Check if today matches a birthday in the birthdays.csv
birthday = pd.read_csv("birthdays.csv")
birthday_month = int(birthday["month"][0])
birthday_day = int(birthday["day"][0])
birthday_name = str(birthday["name"][0])
birthday_mail = str(birthday["email"][0])

today_month = dt.datetime.now().month
today_day = dt.datetime.now().day

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME]
# with the person's actual name from birthdays.csv

if today_month == birthday_month and today_day == birthday_day:
    x = random.randint(1, 3)
    with open(f"./letter_templates/letter_{x}.txt", "r") as file:
        mail = file.readlines()
        y = mail[0].replace("[NAME]", f"{birthday_name}")
        mail[0] = y
        actual_mail = ''.join(mail)
    # 4. Send the letter generated in step 3 to that person's email address.

    with sm.SMTP("smtp.gmail.com") as pipe:
        pipe.starttls()
        pipe.login(user=my_email, password=my_password)
        pipe.sendmail(
            from_addr=my_email,
            to_addrs=birthday_mail,
            msg=f"Subject:Birthday\n\n{actual_mail}"
        )
