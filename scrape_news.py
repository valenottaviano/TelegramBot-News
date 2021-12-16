import requests
from bs4 import BeautifulSoup

def scrapeNews():
  req = requests.get('https://www.lagaceta.com.ar/').text
  soup = BeautifulSoup(req, 'html.parser')

  containers = soup.find_all("div", {"class": "newsRow"})
  content = []

  for container in containers:
    items = container.find_all("div", {"class": "item"})
    for item in items:
      a_tag = item.find_all("div", {"class": "text"})[0].find('a')
      title = a_tag.text
      href = a_tag['href']

      content.append({
        "title": title,
        "href": href
      })

  return content