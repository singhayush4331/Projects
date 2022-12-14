from bs4 import BeautifulSoup
import requests as r

web = r.get("https://news.ycombinator.com")
# print(web.text)

soup = BeautifulSoup(web.text, "html.parser")

# Top headline
headlines = soup.findAll(name="a", class="titlelink", href=True)
link = []
text = []
# highest_points = 0
for headline in headlines:
    link.append(headline['href'])
    text.append(headline.getText())

points = [int(score.getText().split()[0]) for score in soup.findAll(name="span", class="score")]
# for i in points:
#     if i > highest_points:
#         highest_points = i
highest_points = max(points)
top_news_index = points.index(highest_points)
top_news = text[top_news_index]
top_news_link = link[top_news_index]
print(top_news)
print(top_news_link)
print(highest_points)










































# from bs4 import BeautifulSoup
#
#
# with open("website.html", encoding="utf-8") as data:
#     contents = data.read()
#     print(contents)
#
# soup= BeautifulSoup(contents, "html.parser")
# print(soup.prettify())
# heading = soup.findAll(class_="heading")
# print(heading)


