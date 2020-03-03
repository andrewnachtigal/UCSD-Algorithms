# starting a selenium session
# command-i to run script (script:run)
from time import sleep
from selenium import webdriver

# start a new chrome browser session
browser = webdriver.Chrome()

# navigate to a webpage
browser.get('https://www.instagram.com')

# ensure browser stays open 5 seconds
sleep(5)

# clean exit
browser.close()
