import requests, bs4, time
response = requests.get("https://www.36kr.com/newsflashes")
response.encoding = "UTF-8"
soup = bs4.BeautifulSoup(response.text,"lxml")
data1 = soup.find_all(name="div", class_="article")
for n in data1:
    data2 = n.find_all(name="a")
    print("--------------------------------------")
    print("题目:"+data2[0].text)
    print("摘要:"+data2[1].text)
    print("主题:"+data2[2].text)
