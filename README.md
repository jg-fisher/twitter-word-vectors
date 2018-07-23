# twitter-word-vectors
Vectorizes words in a twitter users timeline with word2vec.

$ virtualenv env
$ source env/bin/activate
$ pip install -r requirements.txt
$ PYTHONHASHSEED=123 python analyzer.py user_screen_name

If no parameter is passed for user_screen_name, analysis will run on realDonaldTrump.

Sentiment analysis function is also included.
