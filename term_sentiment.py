## Import sys and json libraries
import sys
import json

## Define main method that calculates sentiment scores for unknown terms
def main():
	## Build dictionary of known sentiment scores for words
    sentdata = open(sys.argv[1])
    scores = {}
    for line in sentdata:
		term, score = line.split("\t")
		scores[term] = int(score)

	## Build list of tweets from twitter data file
    tweetdata = open(sys.argv[2])
    tweets_text = []
    for line in twitterdata:
		tweets = json.loads(line)
		raw_text = tweets['text']
		encoded_text = raw_text.encode('utf-8')
		tweets_text.append(encoded_text)

	## Create empty dictionary to contain unknown words and their sentiment scores
    new_words_and_scores = {}

	## Calculate sentiment scores for all tweets, using known sentiment scores for words   
    for text in tweets_text:
		tweet_score = 0
		new_word_counts = {}
		new_word_list = []
		words = text.split( )
		for word in words:
	    	if word in scores:
				tweet_score += scores[word]
	    	else:
				tweet_score = tweet_score
				new_words_and_scores[word] = [] 
				new_word_list.append(word)
				if word in new_word_counts.keys():
		    		new_word_count[word] += 1
				else:
		    		new_word_count = 1
		for word in new_word_list:
	    	new_words_and_scores[word].append(tweet_score)

	## Calculate sentiment scores for unknown words
    for item in new_words_and_scores.keys():
		## Calculate the proportion of overall positive and negative tweets that the word appears in
		## Use that proportion as an approximation of the new word's sentiment score
		pos_count = 0
		neg_count = 0
		for sent_scores in new_words_and_scores[item]:
			if sent_scores > 0:
		    	pos_count += 1
			elif sent_scores < 0:
		    	neg_count += 1
		if neg_count > 0:
	    	new_term_score = pos_count / neg_count
		else:
	    	new_term_score = pos_count
		print item + " " + str(new_term_score)
 

if __name__ == '__main__':
    main()
