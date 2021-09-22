from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

#env variables
clientID = os.getenv("gClientID")
clientSecret = os.getenv("gClientSecret")
accesstoken = os.getenv("GenuisAccessToken")
redirecturi = os.getenv("RedirectUri")
