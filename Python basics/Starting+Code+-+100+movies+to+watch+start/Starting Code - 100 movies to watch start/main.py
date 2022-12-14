import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"


# Write your code below this line 👇

def Reverse(lst):
    data = lst[::-1]
    return data


web = requests.get(URL)
soup = BeautifulSoup(web.text, "html.parser")

movies_data = [movie.getText() for movie in soup.findAll(name="h3", class_="title")]
movies_list = Reverse(movies_data)

with open("movies.txt", "w") as file:
    for movie in movies_list:
        file.write(f"{movie}\n")
