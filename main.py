import requests
from send_email import send_email

topic = "tesla"

api_key = "d9f8e660313c4c9a84503123c88cae47"
url = "https://newsapi.org/v2/everything?" \
      f"q={topic}&" \
      "sortBy=publishedAt&" \
      "apiKey=d9f8e660313c4c9a84503123c88cae47&language=en"

# Make request
req = requests.get(url)

# Get a dictionary with data
content = req.json()

# Access the articles title and description

body = ""

for article in content["articles"][:20]:
    if article["title"] is not None:
        body = "Subject: Today's News" + "\n" + body + article["title"] + "\n" + \
               article["description"] + "\n" + \
               article["url"] + 2*"\n"

body = body.encode('utf-8')
send_email(message=body)