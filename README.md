# Twitter Sentiment Analysis

To gain additional experience using various tools for large-scale data manipulation (and analysis), I've been working through the [Data Manipulation at Scale: Systems and Algorithms](https://www.coursera.org/learn/data-manipulation) course, offered on Coursera by the University of Washington. The first part of the course involved a project to manipulate and analyze live stream data from Twitter (details can be found [here](https://github.com/kghatala/twitterSentimentAnalysis/blob/master/assignment1.html)) using Python. In this repository are the files that I wrote for this assignment. These include:

- 'twitterstream.py' - a script that compiles live stream data from Twitter
- 'tweet_sentiment.py' - calculates the sentiment of a given tweet using a provided dictionary of pre-determined sentiment scores (AFINN-111.txt)
- 'term_sentiment.py' - calculates sentiment scores for terms that are not include in the dictionary of known words
- 'frequency.py' - calculates term frequencies with the Twitter data
- 'happiest_state.py' - finds the happiest state in the US, according to average sentiment score of tweets
- 'top_ten.py' - finds the top ten most popular hashtags within the stream of Twitter data
