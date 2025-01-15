import requests
from plotly import offline
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}

# 请求github获取结果,解析数据
repo = requests.get(url, headers=headers)
response_dict = repo.json()
repo_dicts = response_dict['items']
repo_names, stars = [], []
for repo_dict in repo_dicts:
    repo_names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])

# 可视化渲染
data = [{'type': 'bar','x': repo_names,'y': stars}]
my_layout = {'title': 'gitHub上最受欢迎的Python项目分布图','xaxis': {'title': 'Repository'},'yaxis': {'title': 'Stars'}}
fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='popular_python_project.html')