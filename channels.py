from pymongo import MongoClient

uri = 'mongodb://helloworld:helloworldpassword1@ds139277.mlab.com:39277/binarymonks?authMechanism=SCRAM-SHA-1'
client = MongoClient(uri)
print('Client is : ', client)

db = client.binarymonks
print('Database is: ', db)

collection = db.channels
print('Collection : ', collection)

collection.delete_many({})

channels = [
    {
        "channel": "hacker_news",
        "title": "Hacker News"
    },
    {
        "channel": "tech_meme",
        "title": "Tech Meme"
    },
    {
        "channel": "tech_crunch",
        "title": "Tech Crunch"
    },
    {
        "channel": "mit_tech_review",
        "title": "MIT Tech Review"
    },
    {
        "channel": "slash_dot",
        "title": "Slash Dot"
    },
    {
        "channel": "christian_heilmann",
        "title": 'Christian Heilmann'
    },
    # {
    # 	"channel": "brad_frost",
    # 	"title": "Brad Frost"
    # },
    {
        "channel": "code_blog",
        "title": "Code Blog"
    },
    {
        "channel": "coding_horror",
        "title": "Coding Horror"
    },
    {
        "channel": "reddit_programming",
        "title": "Reddit Programming"
    },
    {
        "channel": "david_walsh",
        "title": "David Walsh"
    },
    {
        "channel": "joel_on_software",
        "title": "Joel on Software"
    },
    {
        "channel": "sutter_mill",
        "title": "Sutter Mill"
    }
]

result = collection.insert_many(channels)
print('Inserted Channels Ids : ', result)
