#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import json
import texttk
import preprocessfile as ppf

def out_json():
    tweets_data_path = 'data.json'
    
    tweets_data = []
    tweets_file = open(tweets_data_path, "r")
    for line in tweets_file:
        #try:
            #tweets_data.append(tweet['id'])
            if(len(line)<2):
                continue;
            else:
                tweet = json.loads(line)
                tweets_data.append(tweet)
        #except:
        #    continue
    return tweets_data

def addTweet(tweet, list):

    # a dict to contain information about single tweet
    tweet_information={}

    # text of tweet
    tweet_information['text']= ppf.preprocess(tweet['text'])

    # date and time at which tweet was created
    tweet_information['created_at']=tweet['created_at'] #.strftime("%Y-%m-%d %H:%M:%S")

    # id of this tweet
    tweet_information['id']=tweet['id']

    # retweet count
    tweet_information['retweet_count']=tweet['retweet_count']

    # user information in user dictionery
    user_dictionery=tweet['user']

    # screename of the person who tweeted this
    tweet_information['user_id']=user_dictionery['id']
    tweet_information['screen_name']={}
    tweet_information['screen_name']['posted_by']=user_dictionery['screen_name']
    i=1
    while(len(tweet['entities']['user_mentions'])>0 and len(tweet['entities']['user_mentions'])>=i):
        tweet_information['screen_name']['mentioned_{}'.format(i)]=tweet['entities']['user_mentions'][i-1]['screen_name']
        i+=1


    # add this tweet to the tweet_list
    list.append(tweet_information)


def store_tweets(alltweets,file='tweets.json'):

    # a list of all formatted tweets
    tweet_list=[]
    tweet_dict={}
    for tweet in alltweets:

        if('limit' in tweet.keys()):
            continue

        # check if retweeted tweet
        if('retweeted_status' in tweet.keys()):
            tweet = tweet['retweeted_status']
        
        addTweet(tweet, tweet_list)

    tweet_dict["json"] = tweet_list

    # open file desc to output file with write permissions
    file_des=open(file,'wb')

    # dump tweets to the file
    json.dump(tweet_dict,file_des,indent=4,sort_keys=True)

    # close the file_des
    file_des.close()
    
    
    
if __name__ == '__main__':

    # pass in the username of the account you want to download
    alltweets=out_json()
    #print alltweets
    # store the data into json file
#    if len(sys.argv[2])>0:
    store_tweets(alltweets,"final_output.json")
    
    
    