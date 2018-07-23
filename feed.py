from random import shuffle
import feedparser
from pymongo import MongoClient
from moment import Moment
from datetime import datetime
import pytz

# Function to fetch the rss feed and return the parsed RSS
def parseRSS( rss_url ):
    return feedparser.parse( rss_url ) 
    
# Function grabs the rss feed headlines (titles) and returns them as a list
def getHeadlines( channel, rss_url ):
    headlines = []
    
    feed = parseRSS( rss_url )
    for newsitem in feed['items']:
        newsitem['channel'] = channel
        headlines.append(newsitem)
    
    return headlines


def date_sorter(left, right):
    return Moment(left).format('X') - Moment(right).format('X')

# A list to hold all headlines
allheadlines = []

# List of RSS feeds that we will fetch and combine
newsurls = {
    'code_blog': 'https://codeblog.jonskeet.uk/feed/',
    'coding_horror': 'https://feeds.feedburner.com/codinghorror',
    'reddit_programming': 'https://www.reddit.com/r/programming/.rss',
    # 'a_list_apart': 'http://alistapart.com/site/rss', --> Too late
    # 'cat_on_mat': 'http://feeds2.feedburner.com/catonmat',    --> content too long
    'david_walsh': 'https://davidwalsh.name/feed',
    'joel_on_software': 'https://www.joelonsoftware.com/feed/',
    'sutter_mill': 'https://herbsutter.com/feed/',
    # 'steve_yegge': 'http://steve-yegge.blogspot.com/feeds/posts/default',  --> Too late
    'hacker_news': 'https://news.ycombinator.com/rss',
    'tech_crunch': 'http://feeds.feedburner.com/TechCrunch/',
    'tech_meme': 'https://www.techmeme.com/feed.xml',
    'mit_tech_review': 'https://www.technologyreview.com/stories.rss',
    'slash_dot': 'http://rss.slashdot.org/Slashdot/slashdotMain'
    # 'brad_frost': 'bradfrost.com/feed/'
}

def format_published(input_datetime_str):
    moment_obj = Moment(datetime.now()).format('DD MMMM YYYY HH:mm:ss')
    if input_datetime_str:
        moment_obj = Moment(input_datetime_str).format('DD MMMM YYYY HH:mm:ss')
    return moment_obj

# Iterate over the feed urls
for key, url in newsurls.items():
    # Call getHeadlines() and combine the returned headlines with allheadlines
    allheadlines.extend(getHeadlines(key, url))

uri = 'mongodb://helloworld:helloworldpassword1@ds139277.mlab.com:39277/binarymonks?authMechanism=SCRAM-SHA-1'
client = MongoClient(uri)
print('Client is : ', client)

db = client.binarymonks
print('Database is: ', db)

collection = db.feeds
print('Collection : ', collection)

collection.delete_many({})
    
# Iterate over the allheadlines list and print each headline
feed = []
for hl in allheadlines:
    feeditem = {
        'title': hl['title'],
        'link': hl['link'],
        'summary': hl.get('summary', ''),
        'channel': hl['channel'],
        'author': hl.get('author', ''),
        'published': format_published(hl.get('published', None))
    }

    feed.append(feeditem)

# shuffling the feed
shuffle(feed)

print('Feed before : ', [o['published'] for o in feed[1:10]])

feed.sort(key=lambda d: d['published'], reverse=True)

result = collection.insert_many(feed)
print('Inserted Ids : ', result)
