import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'}

# 네이버 데이터랩 사이트의 Top10 검색어를 시간대별로 가져온다.
# Home 에서 시간대별로 호출하여 검색어를 갱신할 수 있다.


def get_ranking_item(year, month, day, hour, min):
    url = f"https://datalab.naver.com/keyword/realtimeList.naver?datetime={year}-{month}-{day}T{hour}%3A{min}%3A00"
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, "html.parser")

    ranking_items = soup.find("ul", {"class": "ranking_list"}).find_all(
        "span", {"class": "item_title_wrap"})

    ranking_item = []

    for item in ranking_items:
        ranking_item.append(item.find("span").string)

    return ranking_item
