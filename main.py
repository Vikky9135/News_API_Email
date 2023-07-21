import requests

api_key = "d9f8e660313c4c9a84503123c88cae47"
url = "https://newsapi.org/v2/everything?q=tesla&from \
        =2023-06-21&sortBy=publishedAt&apiKey=d9f8e660313c4c9a84503123c88cae47"

# Make request
req = requests.get(url)

# Get a dictionary with data
content = req.json()

# Access the articles title and description
for article in content["articles"]:
    print(article["title"])
    print(article["description"])
