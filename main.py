import requests
from send_email import send_email

api_key = "d9f8e660313c4c9a84503123c88cae47"
url = "https://newsapi.org/v2/everything?q=tesla&from \
        =2023-06-21&sortBy=publishedAt&apiKey=d9f8e660313c4c9a84503123c88cae47"

# Make request
req = requests.get(url)

# Get a dictionary with data
content = req.json()

# Access the articles title and description

body = ""

for article in content["articles"]:
    if article["title"] is not None:
        body = body + article["title"] + "\n" + article["description"] + 2*"\n"

body = body.encode('utf-8')
send_email(message=body)