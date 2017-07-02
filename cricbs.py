import requests,bs4
x = "http://www.espncricinfo.com/ci/engine/match/index.html?date="
date = input("\nWhat is the date(yyyy-mm-dd) of the match?")
url1 = x + date
res=requests.get(url1)
res.raise_for_status()
soup=bs4.BeautifulSoup(res.text,"html.parser")
first=soup.select('.innings-info-1')
second=soup.select('.innings-info-2')
status=soup.select('.match-status')
print ("\n")
print (first[0].getText())
print (second[0].getText())
print (status[0].getText())
