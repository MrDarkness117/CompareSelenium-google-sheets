# CompareSelenium-google-sheets
A small Selenium app with checking errors on web pages by searching for them.

I made this simple script to compare two tables in google sheets. I could do it without Selenium by retreiving info using Requests but I decided to make it this way for fun.

Another (the proper) way of doing this would be something like this:

```
import html
import requests

column1 = ['https://google.com', 'https://noone.ru', 'etc']
column2 = ['https://some-broken-link.com', ...]
report = ''

for url in column1:
  for link in column2:
    r = requests.get(url)
    if link in r:
      report += 'found {} in {} \n'.format(link, url)

print(report)
```
