import tweepy as tw
# your Twitter API key and API secret
my_api_key = "fLZX4fZDMZFzJdki8MSaDbVpD"
my_api_secret = "TcIpw1xhzovVaCgUDgYqWLjBGG4dCiYSxfRNh0yg1dbTkUHHhg"
# authenticate
auth = tw.OAuthHandler(my_api_key, my_api_secret)
api = tw.API(auth, wait_on_rate_limit=True)