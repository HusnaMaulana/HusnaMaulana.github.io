import requests
import json
from bs4 import BeautifulSoup
from datetime import datetime

this_time = datetime.now()
waktu = this_time.strftime("%d/%m/%y %H:%M:%S")

page = requests.get("https://www.republika.co.id/")

obj = BeautifulSoup(page.text, 'html.parser');

print ('Menampilkan objek HTML')
print ('======================')
print (obj)

print ('\nMenampilkan title browser dengan tag')
print ('======================================')
print (obj.title)

print ('\nMenampilkan title browser tanpa tag')
print ('======================================')
print (obj.title.text)

print ('\nMenampilkan semua tag h2')
print ('==========================')
print (obj.find_all('h2'))

print ('\nMenampilkan semua text h2')
print ('===========================')
for headline in obj.find_all('h2'):
	print (headline.text)

print ('\nMenampilkan headline berdasarkan div class')
print ('============================================')
print (obj.find_all('div',class_='bungkus_txt_headline_center'))

print ('\nMenampilkan semua text headline')
print ('=================================')
for headline in obj.find_all('div',class_='bungkus_txt_headline_center'):
	print (headline.find('h2').text)

print ('\nMenampilkan headline berdasarkan div class')
print ('============================================')
print (obj.find_all('div',class_='conten1'))

print ('\nMenampilkan semua text headline')
print ('=================================')
for terkini in obj.find_all('div',class_='conten1'):
	print (terkini.find('h1').text)
	print (terkini.find('h2').text)
	print (terkini.find(class_='date').text)

print('\nMenampilkan waktu scrapping')
print('=============================')
print("Current Time = ", waktu)

# Import Package Json
data = []

print ('\nMenampilkan headline pada file json')
print ('=====================================')
f=open('C:\HDD\Web\headline.json','w')
for terkini in obj.find_all('div',class_='conten1'):
	data.append({"topik":terkini.find('h1').text,"judul":terkini.find('h2').text,"waktu_publish":terkini.find(class_='date').text,"waktu_scraping":this_time.strftime("%Y-%m-%d %H:%M:%S")})

jdumps = json.dumps(data)
f.writelines(jdumps)
f.close()

