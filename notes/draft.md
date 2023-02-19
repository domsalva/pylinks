# pylinks

pylinks is a Python script that extracts links from a given webpage using the BeautifulSoup library.

## Features

- **Extracts all links** from a given webpage
- **Saves links to a text file** in the same directory as the script
- Uses regular expressions to **identify links** that uses **"http" or "https"**
- Can **handle any webpage** that can be accessed using a URL

## Requirements

- Python 3.x

If you don't have Python installed, follow these steps:

```bash
sudo apt-get update && sudo apt-get install python3 -y
python3 --version
```

## Installation

```bash
git clone https://github.com/domsalvador/pylinks
cd pylinks
```

## Usage

```bash
python3 pylinks.py 
```

## Sample Usage

```bash
$ python3 pylinks.py
Enter a URL: https://en.wikipedia.org/wiki/Ada_Lovelace

$ ls -CF
README.md  links.txt  notes/  pylinks.py

$ nano links.txt
```
