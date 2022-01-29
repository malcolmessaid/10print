import requests
from bs4 import BeautifulSoup
import pandas as pd


url = 'http://americanbookreview.org/100bestlines.asp'
re = requests.get(url)
soup = BeautifulSoup(re.text, "html.parser")

lines = soup.find("div", {"id": "content"}).findAll('p')

for i, line in enumerate(lines):
    index = (line.text).index(". ")
    lines[i] = line.text[index + 2:].strip()

print(lines)
df = pd.DataFrame(lines)
df.to_csv("lines.csv")
