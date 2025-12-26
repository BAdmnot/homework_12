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
        # print(responce, "\n\n")
        content_dict = responce.json()
        articles = content_dict["articles"]

        email_body = ""
        for article_dict in articles:
            email_body = email_body + article_dict["title"] + "\n" + article_dict["url"] + "\n"*2

        return email_body


if "__main__" == __name__:
    new_feed = NewsFeed(interests="yoga", from_date="2025-12-04", to_date="2025-12-05", language="en")
    # print(new_feed.base_url)
    # print(new_feed.search_in)
    # print(new_feed.api_url)
    # print(new_feed.language)
    print(new_feed.get_news())