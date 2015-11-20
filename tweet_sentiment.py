## Load sys and json libraries
import sys
import json

## Main method to determine the sentiment score of a particular tweet
def main():
	## Load files of sentiment scores (AFINN-111.txt) and twitter data (output from twitterstream.py)
	sentdata = open(sys.argv[1])
	tweetdata = open(sys.argv[2])

	## Accumulate sentiment scores into a dictionary
	scores = {}
	for line in sentdata:
		term, score = line.split("\t")
		scores[term] = int(score)

	## Accumulate text of tweets into a list, with text encoded
	tweets_text = []
	for lines in tweetdata:
		tweets = json.loads(lines)
		text = tweets['text']
		tweets_text.append(text.encode('utf-8'))

	## Loop through twitter data, calculate and print a sentiment score for the text of each tweer
	for tweet in tweets_text:
		split_text = tweet.split( )
		tweet_score = []
		for word in split_text:
			if word in scores:
				tweet_score.append(scores[word])
		final_score = sum(tweet_score)
    	print final_score

if  __name__ == '__main__':
        main()
