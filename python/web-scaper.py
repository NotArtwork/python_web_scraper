from bs4 import BeautifulSoup
import requests

url = "https://www.newegg.com/p/N82E16834156425?Item=N82E16834156425"

result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")

prices = doc.find_all(text="$")
parent = prices[0].parent
strong = parent.find("strong")

for i in prices:
    print(prices[i])
