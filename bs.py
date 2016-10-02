# -*- coding:utf-8 -*-

from bs4 import BeautifulSoup
import urllib

url = 'http://pi.etude.me'
f = urllib.urlopen(url)
soup = BeautifulSoup(f.read()) 

print soup

codes = soup.find_all('code')
print codes

for code in codes:
    print code.text
    print ''

