import requests

url = "https://api.github.com/search/repositories?q=language:python&sort=stars"

headers = {'Accept': 'application/vnd.github.v3+json'}
repos = requests.get(url, headers=headers)
print(f"Status code :{repos.status_code}")

# 接收返回值
response_dict = repos.json()
print(response_dict.keys())