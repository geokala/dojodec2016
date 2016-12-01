import requests
import bs4
from textblob import TextBlob
import random


URL = 'https://twitter.com/realDonaldTrump'
US_STATES = ['ALABAMA', 'ALASKA', 'ARIZONA', 'ARKANSAS', 'CALIFORNIA', 'COLORADO', 'CONNECTICUT', 'DELAWARE', 'DISTRICT OF COLUMBIA', 'FLORIDA', 'GEORGIA', 'HAWAII', 'IDAHO', 'ILLINOIS', 'INDIANA', 'IOWA', 'KANSAS', 'KENTUCKY', 'LOUISIANA', 'MAINE', 'MARYLAND', 'MASSACHUSETTS', 'MICHIGAN', 'MINNESOTA', 'MISSISSIPPI', 'MISSOURI', 'MONTANA', 'NEBRASKA', 'NEVADA', 'NEW HAMPSHIRE', 'NEW JERSEY', 'NEW MEXICO', 'NEW YORK', 'NORTH CAROLINA', 'NORTH DAKOTA', 'OHIO', 'OKLAHOMA', 'OREGON', 'PENNSYLVANIA', 'RHODE ISLAND', 'SOUTH CAROLINA', 'SOUTH DAKOTA', 'TENNESSEE', 'TEXAS', 'UTAH', 'VERMONT', 'VIRGINIA', 'WASHINGTON', 'WEST VIRGINIA', 'WISCONSIN', 'WYOMING']
COMMUNIST_STATES = [
    'Moscow',
    'Tirana',
    'Beijing',
    'Pyongyang',
    'Ulan Bator',
    'Ha Noi',
    'Phnom Penh',
    'Warsaw',
    'Vientiane',
    'Belgrade',
    'Budapest',
    'Mahabad',
    'Sofia',
    "Yan'an",
    'Kyzyl',
    'Aden',
    'Tabriz',
    'Helsinki',
    'East Berlin',
    'Havana',
]


def change_tweet_noun(tweet):
    blob = TextBlob(tweet)
    for noun in blob.noun_phrases:
        if noun.upper() in US_STATES:
            fixed_tweet = str(blob).upper().replace(noun.upper(), random.choice(COMMUNIST_STATES))

    return fixed_tweet.lower()


def get_tweets():
    response = requests.get(url=URL)
    data = bs4.BeautifulSoup(response.text, 'html.parser')
    tweets_html = data.find_all('p', 'js-tweet-text')
    tweets = [tweet.findAll(text=True)[0] for tweet in tweets_html]

    tweets = change_tweet_noun(tweets[0])

    return tweets

tweets = get_tweets()
print(tweets)

