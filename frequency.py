## Load sys and json libraries
import sys
import json

## Define main method to calculate frequencies of words across twitter data
def main():
	## Read in and encode text of tweets from twitter data file
    tweetdata = open(sys.argv[1])
    tweets_text = []
    for line in tweetdata:
		tweets = json.loads(line)
		raw_text = tweets['text']
		encoded_text = raw_text.encode('utf-8')
		tweets_text.append(encoded_text)
    
    ## Create empty dictionary to track word frequencies
    word_frequencies = {}

    ## Loop through text of tweets and calculate word frequencies
    for tweet in tweets_text:
		words = tweet.split( )
		for word in words:
	    	if word in word_frequencies.keys():
				word_frequencies[word] += 1
	    	else:
				word_frequencies[word] = 1
    
    ## Print word frequencies within entire data set
    for key in word_frequencies.keys():
		print key + " " + str(word_frequencies[key])

if __name__ == '__main__':
    main()
