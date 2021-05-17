import requests
import html

api_request = requests.get("https://opentdb.com/api.php?amount=10&type=boolean")

data = api_request.json()

question_data = html.unescape(data['results'])

print(question_data)