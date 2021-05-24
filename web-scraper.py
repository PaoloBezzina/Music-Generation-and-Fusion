# Import libraries
import os
import requests
from bs4 import BeautifulSoup

# getting url's
midiFiles = []
f = open("Sites-to-scrape-from/Music by John Williams.html", "r")
html = f.read()

soup = BeautifulSoup(html, 'html.parser')

for a in soup.find_all('a', href=True):
    link = a['href']
    if link.endswith('.mid'):
        if "piano" in link:
            midiFiles.append(link)
            print ("Found the URL:", link)

# downloading files
for file in midiFiles:
    r = requests.get(file, allow_redirects=True, verify=False)
    with open(os.path.join('Scraper-Files', os.path.basename(file)), 'wb') as f:
        f.write(r.content)