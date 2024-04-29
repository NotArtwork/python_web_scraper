from bs4 import BeautifulSoup
import requests

url = "https://www.newegg.com/p/N82E16834156425?Item=N82E16834156425"

result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")
print(doc.prettify())