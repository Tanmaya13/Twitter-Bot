import tweepy as tw

consumer_key = 'enter_your_consumer_key'
consumer_secret = 'your_consumer_secret'
access_token = 'your_access_token'
access_token_secret = 'your_access_token_secret'

auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
  
api = tw.API(auth)        # calling the API


public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)               # it will print all the public tweets that comes to my twiiter, in console(command prompt)



user = api.get_user(screen_name="your_screenname")
print('USER DETAILS ARE: ')
print(user.name)                                    # my name in twitter
print(user.screen_name)                             # my twitter id
print(user.followers_count)                         # my number of followers in twitter
for friend in user.friends():
    print(friend.screen_name)                       # names of all followings

for follower in tw.Cursor(api.get_followers).items():    
    follower.follow()                                    # it will increase the following section depending the number of followers
                                                            # if following=7 and follower=10 and you have not followed any of the 10 ppl
                                                            # then after running this code, folloing will show '17' (7+10) in Twitter account


api.create_favorite('id_of_the_tweet')              # it will like the tweet that I have posted on twitter
                                                         # it will only work once on each post, as you cannot like a tweet multiple times

api.destroy_favorite('id_of_the_tweet')             # it will dislike the tweet that is previously liked by me and others
