# pylinks

pylinks is a Python script that extracts links from a webpage URL

[![demo.jpg](https://raw.githubusercontent.com/Db-San/pylinks/main/demo/demo.gif)](https://asciinema.org/a/561072)

- **Extracts all links** from a given webpage
- **Saves links to a text file** in the same directory as the script
- Uses regular expressions to **identify links** that uses **"http" or "https"**
- Can **handle any webpage** that can be accessed using a URL

## Requirements Installation and Usage

```bash
sudo apt-get update && sudo apt-get install python3 python3-pip git -y
git clone https://github.com/domsalva/pylinks
cd pylinks
pip install -r requirements.txt
python3 pylinks.py
```

## Sample Usage

```bash
$ python3 pylinks.py
pylinks / github
-------------------
Enter a URL
> https://en.wikipedia.org/wiki/Ada_Lovelace
Links written to links.txt

$ ls
demo  links.txt  pylinks.py  README.md  requirements.txt  sorted.txt

$ cat links.txt | grep org > sorted.txt
$ cat sorted.txt
```
