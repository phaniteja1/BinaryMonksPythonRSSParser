from pymongo import MongoClient

uri = 'mongodb://helloworld:helloworldpassword1@ds139277.mlab.com:39277/binarymonks?authMechanism=SCRAM-SHA-1'
client = MongoClient(uri)
db = client.binarymonks
collection = db.channels

channels = [
    {
        "channel": "hacker_news",
        "title": "Hacker News"
    },
    {
        "channel": "reddit_programming",
        "title": "Reddit Programming"
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
    {
        "channel": "echo_js",
        "title": "Echo JS"
    },
    {
        "channel": "a_list_apart",
        "title": "A List Apart"
    },
    {
        "channel": "bruce_lawson",
        "title": "Bruce Lawson"
    },
    {
        "channel": "hey_designer",
        "title": "Hey Designer"
    },
    {
        "channel": "treehouse_blog",
        "title": "Treehouse Blog"
    },
    {
        "channel": "cats_who_code",
        "title": "Cats Who Code"
    },
    {
        "channel": "remy_sharp",
        "title": "Remy Sharp"
    },
    {
        "channel": "snook",
        "title": "Snook.ca"
    },
    {
        "channel": "ben_nadel",
        "title": "Ben Nadel"
    },
    {
        "channel": "site_point",
        "title": "Site Point"
    },
    # {
    #     "channel": "github_blog",
    #     "title": "Github Blog"
    # },
    {
        "channel": "javascript_weekly",
        "title": "Javascript Weekly"
    },
    {
        "channel": "sidebar",
        "title": "Sidebar"
    },
    # {
    #     "channel": "cloud_four",
    #     "title": "Cloud Four"
    # },
    {
        "channel": "adactio",
        "title": "Adactio"
    },
    {
        "channel": "functioning_form",
        "title": "Functioning Form"
    },
    {
        "channel": "impressive_webs",
        "title": "Impressive Webs"
    },
    {
        "channel": "jens_o_meiert",
        "title": "Jens O Meiert"
    },
    {
        "channel": "coding_confessions",
        "title": "Coding Confessions"
    },
    # {
    # 	"channel": "brad_frost",
    # 	"title": "Brad Frost"
    # },
    # {
    #     "channel": "code_blog",
    #     "title": "Code Blog"
    # },
    # {
    #     "channel": "coding_horror",
    #     "title": "Coding Horror"
    # },
    {
        "channel": "david_walsh",
        "title": "David Walsh"
    },
    {
        "channel": "joel_on_software",
        "title": "Joel on Software"
    },
    # {
    #     "channel": "sutter_mill",
    #     "title": "Sutter Mill"
    # }
]

def run_and_insert():
    # clean all the current channels
    collection.delete_many({})

    result = collection.insert_many(channels)
    print('Inserted Channels Ids : ', result)
