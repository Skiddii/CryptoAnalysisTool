from bs4 import BeautifulSoup
import requests
import time

page_to_scrape = requests.get("https://crypto.com/price")
soup = BeautifulSoup(page_to_scrape.text, "html.parser")

while True:
    cryptoNames = soup.findAll("p", attrs={"class":"chakra-text css-rkws3"})
    count = 1
    for cryptoName in cryptoNames:
        print(count, cryptoName.text)
        count+=1
    time.sleep(60)
