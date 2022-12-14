# from bs4 import BeautifulSoup
# import requests as r
#
# URL = "https://www.billboard.com/charts/hot-100/"
#
# date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
#
# web = r.get(URL+date)
# soup = BeautifulSoup(web.text, "html.parser")
#
# songs_list = [song.getText() for song in soup.find_all("span", class_="chart-element__information__song")]
#
# print(songs_list)
from bs4 import BeautifulSoup
import requests

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

response = requests.get("https://www.billboard.com/charts/hot-100/" + date)

soup = BeautifulSoup(response.text, 'html.parser')
song_names_spans = soup.find_all("span", class_="chart-element__information__song")
song_names = [song.getText() for song in song_names_spans]
print(song_names)
