import requests
import csv

# 配置API信息，把这里的'YOUR_API_KEY'替换成你自己的API Key，城市可以改成你想要的
api_key = '72ad2eca21e53fbee64d56d0a5a86499'
city = 'Taipei'
url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'

# 发送请求获取数据
response = requests.get(url)
data = response.json()

# 提取需要的天气数据
weather_data = {
    'city': city,
    'temperature': data['main']['temp'],
    'humidity': data['main']['humidity'],
    'description': data['weather'][0]['description'],
    'wind_speed': data['wind']['speed']
}

# 将天气数据保存为CSV文件
with open('api.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=weather_data.keys())
    writer.writeheader()
    writer.writerow(weather_data)