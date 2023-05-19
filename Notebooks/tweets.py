import snscrape.modules.twitter as sntwitter
import pandas as pd

query = "(eth OR ethereum) min_replies:10 min_faves:300 min_retweets:30 until:2023-03-28 since:2019-01-01"
tweets = []
limit = 10000


for tweet in sntwitter.TwitterSearchScraper(query).get_items():
    
    # print(vars(tweet))
    # break
    if len(tweets) == limit:
        break
    else:
        tweets.append([tweet.date, tweet.username, tweet.content])
        
df = pd.DataFrame(tweets, columns=['Date', 'User', 'Tweet'])
print(df)

# to save to csv
df.to_csv('tweetsethereum3.csv')