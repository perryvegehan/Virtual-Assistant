# Web scraping is the process of gathering data from the internet automatically
# what we do in web scraping is we grab a html section from a website
# as every websit is unique, so is it's web scraping script.

# A web-site consists of 3 parts: HTML CSS and JS
#  HTML is used to create the basic layout and structure of the website
#  CSS is used to pprovide designs
#  JavaScript is used to control the interactive elements of the website.

# for web scraping we need to install 3 libraries: requests, lxml and bs4
import requests
import lxml
import bs4

# now let us open a webpage. Example.com--->>> It is a demo webpage

web_page=requests.get("http://example.com/")
#print(web_page.text) # This line actually prints out the raw html text

# To make the text more readable, we will use the bs4 or the Beautiful Soup
soup=bs4.BeautifulSoup(web_page.text,"lxml")
print(soup)


