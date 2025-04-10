import requests
from bs4 import BeautifulSoup
import json

# 初始化一个空列表，用来存储电影信息
movies = []
# 豆瓣电影Top250分10页展示，每页25条数据，通过循环遍历每一页
for start in range(0, 250, 25):
    url = f'https://movie.douban.com/top250?start={start}'
    # 设置请求头，模拟浏览器访问，避免被网站拒绝
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'}
    response = requests.get(url, headers=headers)
    # 使用BeautifulSoup解析网页内容
    soup = BeautifulSoup(response.text, 'html.parser')

    # 找到每个电影的信息块，并提取需要的信息
    for item in soup.find_all('div', class_='item'):
        title = item.find('span', class_='title').text
        rating = item.find('span', class_='rating_num').text
        info = item.find('div', class_='bd').p.text.strip().split('\n')[0]
        movies.append({
            'title': title,
            'rating': rating,
            'info': info
        })

# 将电影信息保存为JSON文件
with open('static.json', 'w', encoding='utf-8') as f:
    json.dump(movies, f, ensure_ascii=False, indent=4)