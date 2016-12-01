import requests
import bs4


URL = 'https://twitter.com/realDonaldTrump'


def get_tweets():
    response = requests.get(url=URL)
    data = bs4.BeautifulSoup(response.text, 'html.parser')
    tweets_html = data.find_all('p', 'js-tweet-text')
    tweets = [tweet.findAll(text=True)[0] for tweet in tweets_html]

    return tweets

tweets = get_tweets()
print(tweets)

