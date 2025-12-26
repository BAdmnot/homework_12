import requests
from config import API_KEY


class NewsFeed:
    """Representing multiple news titles and links as a single string."""
    base_url = "https://newsapi.org/v2/everything?"
    search_in = "title,description"
    api_url = API_KEY

    def __init__(self, interests, from_date, to_date, language="en"):
        self.interests = interests
        self.from_date = from_date
        self.to_date = to_date
        self.language = language

    def get_news(self):
        url = (
            f"{self.base_url}"
            f"q={self.interests}&"
            f"searchIn={self.search_in}&"
            f"from={self.from_date}&"
            f"to={self.to_date}&"
            f"language={self.language}&"
            f"apiKey={self.api_url}"
        )

        responce = requests.get(url)
        if responce.status_code != 200 or 'articles' not in responce.json().keys():
            return f'<h3>Unfortunately, an error occurred.</h3>\n<span style="color: red">Code: {responce.status_code}.</span>\n\n\n <b>You can contact our developer team: <a href="mailto:bogdan.artvas@gmail.com">bogdan.artvas@gmail.com</a></b>'
        content_dict = responce.json()
        articles = content_dict["articles"]

        email_body = ""

        if len(articles) == 0:
            email_body = f"Unfortunately, no fresh news was found on the topic {self.interests} in the last 24 hours."
        else:
            for article_dict in articles:
                email_body = email_body + f"<a href='{article_dict["url"]}'> {article_dict['title']}</a>\n\n"

        return email_body