import tweepy
import requests
import json
import twitter_info	


## SI 206 - HW
## COMMENT WITH:
## Your section day/time: 001 Wednesday 6PM
## Any names of people you worked with on this assignment: Jack Stephenson (me)

# Authentication info below, found in twitter_info.py file
consumer_key = twitter_info.consumer_key
consumer_secret = twitter_info.consumer_secret
access_token = twitter_info.access_token
access_token_secret = twitter_info.access_token_secret
# Set up your authentication to Twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
# Set up library to grab stuff from twitter with your authentication, and 
# return it in a JSON-formatted way

# Set up library to grab stuff from twitter with your authentication, and return it in a JSON format 
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser()) 

# Name cache file 
CACHE_FNAME = "StephensonTwitterCache.json"


try:
    cache_file = open(CACHE_FNAME, 'r') # Try to read the data from the file
    cache_contents = cache_file.read()  # If it's there, get it into a string
    CACHE_DICTION = json.loads(cache_contents) # And then load it into a dictionary
    cache_file.close() # Close the file, we're good, we got the data in a dictionary.
except:
    CACHE_DICTION = {}

# Input: a string
# Output: dictionary of top 5 results from tweepy search on inputted string
# Saves output to cache file; checks cache file for output data before executing tweepy call
def getTwitWithCaching(qwt):
	if qwt in CACHE_DICTION:
		print("Data was in the cache")
		return CACHE_DICTION[qwt]
	else:
		print("fetching")
		uh = api.search(q=qwt)
		returnies = []
		try:
			for i in range(5):
				text = uh["statuses"][i]["text"]
				created_at = uh["statuses"][i]["created_at"]
				returnies.append({"TEXT": text, "CREATED AT": created_at})
				CACHE_DICTION[qwt] = returnies
				dumped_json_cache = json.dumps(CACHE_DICTION)
				fw = open(CACHE_FNAME,"w")
				fw.write(dumped_json_cache)
			i = 0
			fw.close() # Close the open file
			return CACHE_DICTION[qwt]
		except:
			print("Wasn't in cache and wasn't valid search either")
			return None


# runs program, asks for input-- prints out output, all 3 times
returndata = []
for i in range(3):
	term = input("Enter Tweet term: ")
	returndata = getTwitWithCaching(term)
	for data in returndata:
		print("TEXT: " + data["TEXT"])
		print("CREATED AT: " + data["CREATED AT"])
		print("\n")
	i = 0









