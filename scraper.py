__author__ = 'Hernan Y.Ke'
import urllib.request
from urllib.parse import urljoin
from bs4 import BeautifulSoup



base_url = "http://apod.nasa.gov/apod/archivepix.html"
dic = "img"
content = urllib.request.urlopen(base_url).read()
for link in BeautifulSoup(content,"lxml").findAll("a"):
    print("For following link",link)
    href = urljoin(base_url,link["href"])
    content = urllib.request.urlopen(href).read()
    for img in BeautifulSoup(content,"lxml").findAll("img"):
        img_href = urljoin(href,img["src"])
        print("Downloading",img_href)
        img_name = img_href.split("/")[-1]
        urllib.request.urlretrieve(img_href,dic+"/"+img_name)
