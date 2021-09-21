# CompareSelenium-google-sheets
A small Selenium app with checking errors on web pages by searching for them.

I made this simple script to compare two tables in google sheets. I could do it without Selenium by retreiving info using Requests but I decided to make it this way for fun.

Another way of doing this would be something like this:

```
import html

r = requests.get('https://google.com')

print(html.unescape(r.text))
```
