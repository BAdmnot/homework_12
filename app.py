import yagmail
import pandas as pd
import datetime
import time

from config import ADMIN_EMAIL_PASSWORD, ADMIN_EMAIL, t_hour, last_date
from news import NewsFeed


while True:
    if datetime.datetime.now().hour >= t_hour and (not last_date or datetime.datetime.now().day > last_date.day):
        df = pd.read_excel("people.xlsx")

        for index, row in df.iterrows():

            today = datetime.date.today().isoformat()
            yesterday = (datetime.date.today() - datetime.timedelta(days=1)).isoformat()

            user_interest = row["interest"]
            user_language = row["language"]

            news_feed = NewsFeed(interests=user_interest, from_date=yesterday, to_date=today, language=user_language)
            email_body = news_feed.get_news()
            mail_contects = f"""<h1>Gooooooooooooooood Morning, Vietnam!</h1><img src="cid:gm_image"><h3>Hi {row['name']},</h3>\n <b>See what's on about {user_interest} today!</b>\n\n {email_body}"""

            email = yagmail.SMTP(user=ADMIN_EMAIL, password=ADMIN_EMAIL_PASSWORD)
            if 'an error occurred' not in email_body: # да, костильно, і шо дальше?
                email.send(
                    to=row["email"],
                    subject=f"Your {user_interest} news are ahead for today!",
                    contents=[mail_contects, yagmail.inline("gm_image.jpg")]
                )
            else:
                email.send(
                    to=row["email"],
                    subject=f"Your {user_interest} news are ahead for today!", #я думав змінити тему, але це не буде правильно, тому залишив
                    contents=email_body
                )

    print(f'Checked ({datetime.datetime.now().hour}:{datetime.datetime.now().minute}:{datetime.datetime.now().second})') # залишив, най буде
    last_date = datetime.datetime.now()
    time.sleep(3600)