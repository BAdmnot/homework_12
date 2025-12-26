import yagmail
import pandas as pd
import datetime
import time

from config import ADMIN_EMAIL_PASSWORD
from news import NewsFeed


while True:
    if datetime.datetime.now().hour == 10 and datetime.datetime.now().minute == 0:
        df = pd.read_excel("people.xlsx")

        for index, row in df.iterrows():
            # print(row, "\n")
            # print(row["interest"], "\n")

            today = datetime.date.today().isoformat()
            yesterday = (datetime.date.today() - datetime.timedelta(days=1)).isoformat()
            # print(today)
            # print(yesterday)

            user_interest = row["interest"]

            news_feed = NewsFeed(interests=user_interest, from_date=yesterday, to_date=today)
            email_body = news_feed.get_news()
            mail_contects = f"Hi {row['name']}\n\n See what's on about {user_interest} today!\n\n {email_body}"

            email = yagmail.SMTP(user="1998ivankaa@gmail.com", password=ADMIN_EMAIL_PASSWORD)
            email.send(
                to=row["email"],
                subject=f"Your {user_interest} news are ahead for today!",
                contents=mail_contects,
            )

    time.sleep(60)