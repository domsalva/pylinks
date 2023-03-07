from bs4 import *
import requests
import re

# Functions
def display_header():
    header = "pylinks / github"
    print(header)
    print("-"*len(header) + "-"*3)

# Main program
display_header()

while True:
    url = input(f"Enter a URL\n> ")
    try:
        response = requests.get(url)
        response.raise_for_status()
        break
    except requests.exceptions.RequestException as e:
        print(f"{e}\n")

soup = BeautifulSoup(response.text, "html.parser")

links = []
for link in soup.find_all("a"):
    href = link.get("href")
    if href and re.match(r"^https?://", href):
        links.append(href)

with open("links.txt", "w") as file:
    for link in links:
        file.write(link + "\n")

print("Saved to links.txt")
