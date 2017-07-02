import sys,webbrowser,requests,bs4
print('Googling...')
res=requests.get('https://www.google.co.in/search?q='+''.join(sys.argv[1:]))
res.raise_for_status()
soup=bs4.BeautifulSoup(res.text)
linkElements=soup.select('.r a')
tabs=min(5,len(linkElements))
for i in range(tabs):
    webbrowser.open('http://google.com' + linkElements[i].get('href'))
