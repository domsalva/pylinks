from bs4 import *
import requests
import re

# Functions
def display_header():
    print("pylinks / github")
    print("-"*25)
    
# Main program
display_header()    
url = input(f"Enter a URL\n> ")

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
    print("Links written to link.txt")
