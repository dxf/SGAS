import feedparser
from time import sleep
from audioplayer import AudioPlayer
pe = ''

while True:
    NewsFeed = feedparser.parse("https://www.gov.uk/search/news-and-communications.atom")
    entry = NewsFeed.entries[0]
    if pe == entry:
        print('Same as before.')
        sleep(5)
    else:
        print('Report?')
        print('Post Title :',entry.title)
        AudioPlayer("censor-beep-1.mp3").play(block=True)
        pe = NewsFeed.entries[0]
        sleep(5)