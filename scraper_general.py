__author__ = 'Hernan Y.Ke'
import urllib.request
import os
from urllib.parse import urljoin
from bs4 import BeautifulSoup



base_url = "http://apod.nasa.gov/apod/archivepix.html"
dic = "img"

to_visit = set((base_url,))
visited = set()
while to_visit:
    current_page = to_visit.pop()
    print("visiting",current_page)
    visited.add(current_page)
    content = urllib.request.urlopen(current_page).read()
    for link in BeautifulSoup(content,"lxml").findAll("a"):
        absolute_link = urljoin(current_page,link["href"])
        if absolute_link not in visited:
            to_visit.add(absolute_link)
        else:
            print("exist already",absolute_link)
    for img in BeautifulSoup(content,"lxml").findAll("img"):
        img_href = urljoin(current_page,img["src"])
        print("Downloading",img_href)
        img_name = img_href.split("/")[-1]
        urllib.request.urlretrieve(img_href,os.path.join(os.path.abspath(dic),img_name))