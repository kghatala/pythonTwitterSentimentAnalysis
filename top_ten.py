## Import required libraries
import sys
import json
import operator

## Define main method to find top ten most popular hashtags in a stream of twitter data
def main():
	## Load twitter data
    tweetdata = open(sys.argv[1])
    raw_tweets = []
    for line in tweetdata:
		tweet = json.loads(line)
		raw_tweets.append(tweet)
	##Create empty dictionary to track the frequencies of various hashtags
    tag_frequencies = {}
    ## Loop through raw tweets that contain hashtags
    for num in range(len(raw_tweets)):
		if all(item in raw_tweets[num].keys() for item in ('text','entities')):
	    	if not (raw_tweets[num]['entities']['hashtags'] == None):
				raw_tags = raw_tweets[num]['entities']['hashtags']
				## Create a list of hashtags contained within the tweet
				htags = []
				for n in range(len(raw_tags)):
		    		encoded_tag = raw_tags[n]['text'].encode('utf-8')
		    		htags.append(encoded_tag)
				## Track frequencies of hashtags within the dictionary created above
				for i in range(len(htags)):
		    		if htags[i] in tag_frequencies.keys():
		        		tag_frequencies[htags[i]] +=1
		    		else:
		        		tag_frequencies[htags[i]] = 1

	## Sort the hashtag frequencies in descending order
    sort_frequencies = sorted(tag_frequencies.items(), key=operator.itemgetter(1), reverse=True)
    
    ## Print the top ten most frequent hashtags, along with their frequencies
    for x in range(10):
    	print str(sort_frequencies[x][0]) + " " + str(sort_frequencies[x][1])


if __name__ == '__main__':
    main()
