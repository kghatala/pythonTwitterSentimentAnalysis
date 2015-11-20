## Load required libraries
import sys
import json

## Define main method to determine the state with the happiest tweets
def main():
	## Load known sentiment and twitter data
    sentdata = open(sys.argv[1])
    tweetdata = open(sys.argv[2])

    ## Build dictionary of known sentiment scores
    scores = {}
    for line in sentdata:
		term, score = line.split('\t')
		scores[term] = int(score)
    
    ## Build list containing all raw twitter data
    tweets_raw = []
    for lines in tweetdata:
		tweets = json.loads(lines)
		tweets_raw.append(tweets)

	## Create empty dictionary to contain sentiment scores for each state
    state_scores = {}

    ## Loop through all tweets, isolating those where 'text' and 'place' fields are complete and the tweet came from the US
    for num in range(len(tweets_raw)):
		if all (item in tweets_raw[num].keys() for item in ('text','place')):
	    	if not (tweets_raw[num]['place'] == None):
				if (tweets_raw[num]['place']['country_code'] == 'US'):
		    		## Extract tweet text and the state in which it originated
		    		words = tweets_raw[num]['text']
		    		split_words = words.split( )
		    		encoded_words = []
		    		for i in range(len(split_words)):
						encoded = split_words[i].encode('utf-8')
						encoded_words.append(encoded)
		    		loc = tweets_raw[num]['place']['name']
		    		loc = loc[-2:]
		    		loc = loc.encode('utf-8')
		    		## Calculate the score for the tweet
		    		tweet_score = []
		    		for word in encoded_words:
	    	        	if word in scores.keys():
			    			tweet_score.append(scores[word])
	    	    	final_score = sum(tweet_score)
		
		    		## Add the sentiment score to the dictionary, matched with its state of origin
		    		if loc in state_scores.keys():
		        		state_scores[loc].append(final_score)
		    		else:
		        		state_scores[loc] = []
		        		state_scores[loc].append(final_score)

	## Determine which state has the highest average sentiment score (the happiest state)
    top_score = 0
    happiest_state = []
    for state in state_scores.keys():
		state_avg = sum(state_scores[state]) / len(state_scores[state])
		if state_avg > top_score or happiest_state == "":
    	    top_score = state_avg
	    	happiest_state = state
    print happiest_state


if __name__ == '__main__':
    main()
