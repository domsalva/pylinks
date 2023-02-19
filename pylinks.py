from bs4 import *
import requests
import re

url = input("Enter a URL: ")

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

links = []
for link in soup.find_all("a"):
    href = link.get("href")
    if href and re.match(r"^https?://", href):
        links.append(href)

with open("links.txt", "w") as file:
    for link in links:
        file.write(link + "\n")
