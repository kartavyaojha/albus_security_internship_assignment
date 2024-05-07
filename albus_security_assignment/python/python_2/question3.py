import requests
url="https://google.com"
res = requests.get(url)
print("status code:",res.status_code)
print("content:",res.content)