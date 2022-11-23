import requests
from bs4 import BeautifulSoup as bs

github_profile = "https://github.com/SiaLater69"
req = requests.get(github_profile)
scrapper = bs(req.content, "html.parser")
profile_picture = scrapper.find("img", {"alt": "Avatar"})["src"]
print(profile_picture)
