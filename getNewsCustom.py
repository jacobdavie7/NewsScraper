import requests #Will NOT run if requests module is not installed on machine running on
import re

print ("Enter URL to grab data from")

site = input()

r = requests.get(site)

news = re.findall(">([^<]+</a></h2>", r.text)

for n in news:
  n = n.encode("ascii", "ignore")
  print (n)
