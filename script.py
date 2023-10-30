import requests
from bs4 import BeautifulSoup
import pprint

res = requests.get('https://news.ycombinator.com/news')
# print(res.text)
soup = BeautifulSoup(res.text,'html.parser')
# print(soup.find(id="score_37994460"))
# print(soup.select('.morelink'))
links = soup.select('.morelink')
subtext = soup.select('.subtext')
# print(votes[1].get('id'))
# print(votes[0])


def create_custome_hn(links, subtext):
    hn =[]
    for idx, item in enumerate(links):
        title = item.getText()
        href = item.get('href', None)
        vote = subtext[idx].select('.score') 
        if len(vote):
            points = int(vote[0].getText().replace('points', ''))
            # print(points)
            hn.append({'title':title, 'link':href, 'votes':points})
    return hn

pprint.pprint(create_custome_hn(links, subtext))