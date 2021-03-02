import requests
#得到百度所有返回数据
respons = requests.get(url="https://www.baidu.com")
respons.encoding = "utf-8"
#提取数据
data = respons.text
#写到html文件里
f = open("百度.html","w+",encoding="utf-8")
f.write(data)