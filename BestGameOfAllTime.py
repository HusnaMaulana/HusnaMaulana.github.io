import json
import urllib.request
from selenium import webdriver
from datetime import datetime

this_time = datetime.now()
waktu = this_time.strftime("%d/%m/%y %H:%M:%S")

PATH = "C:\HDD\Selenium\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://www.metacritic.com/browse/games/score/metascore/all/all/filtered")

BestGameOfAllTime = []
i = 1

for games in driver.find_elements_by_tag_name("tr"):
    print(games.text)
    for banner in games.find_elements_by_tag_name("a"):
        for img in banner.find_elements_by_tag_name("img"):
            print(img.get_attribute("src"))

            BestGameOfAllTime.append(
                {"No": games.text.split("\n")[1],
                 "Title": games.text.split("\n")[2],
                 "Platform": games.text.split("\n")[3],
                 "Release_date": games.text.split("\n")[4],
                 "Rating": games.text.split("\n")[0],
                 'Waktu_scrapping':waktu,
                 "Image": img.get_attribute("src")
                 }
            )
result = open("C:\HDD\Selenium\BestGameOfAllTime.json", "w")
json.dump(BestGameOfAllTime, result, indent = 6)
result.close()

driver.quit()
