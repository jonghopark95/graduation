import requests
from bs4 import BeautifulSoup

chosun = []
donga = []
joongang = []


headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'}


def joongang_scrapper(search_term):
    # 크롤링 대상 URL 가져오기
    joongang_url = f"https://news.joins.com/Search/JoongangNews?Keyword={search_term}&SortType=New&SearchCategoryType=JoongangNews&PeriodType=All&ScopeType=All&ImageType=All&JplusType=All&BlogType=All&ImageSearchType=Image&TotalCount=0&StartCount=0&IsChosung=False&IssueCategoryType=All&IsDuplicate=True&Page=1&PageSize=10&IsNeedTotalCount=True"
    # requests 모듈의 get 함수로 파싱할 사이트 가져오기, 이 때 headers 는 사업 목적이 아닌 개인 목적으로 크롤링 함을 입력
    request = requests.get(joongang_url, headers=headers)
    # 간혹 크롤링 했을 때 문자 깨짐 현상 발생... 이를 방지 하기 위한 encoding 변경
    request.encoding = 'utf-8'
    # 크롤링을 원활히 하게 해주는 BeatufiulSoup를 사용하여 해당 사이트 html 가져옴
    soup = BeautifulSoup(request.text, "html.parser")

    # 기사들을 크롤링함. find로 타고 들어가 li로 묶여있는 여러 기사들을 find_all 하여 배열 형태로 저장
    # 임시로 5개의 기사만 가져오도록 함.
    news_lists_box = soup.find(
        "div", {"class": "section_news"}).find("div", {"class": "bd"}).find_all("li")[0:5]

    # 각 기사별로 제목, 기사 간략 내용 링크를 가져온다.
    for news_list in news_lists_box:
        news_title = news_list.find("h2", {"class": "headline mg"}).getText()
        news_content = news_list.find("span", {"class": "lead"}).getText()
        news_link = news_list.find(
            "h2", {"class": "headline mg"}).find("a")["href"]
        # 임시로 객체를 만들어 놓고, 각 기사별로 외부에 있는 배열에 객체 형태로 값을 저장한다.
        news_box = {}
        news_box['title'] = news_title
        news_box['content'] = news_content
        news_box['link'] = news_link
        # 각 뉴스 객체를 외부 배열에 저장
        joongang.append(news_box)


def chosun_scrapper(search_term):
    chosun_url = f"https://nsearch.chosun.com/search/total.search?query={search_term}&sort=1"
    request = requests.get(chosun_url, headers=headers)
    request.encoding = 'utf-8'

    soup = BeautifulSoup(request.text, "html.parser")
    search_news_box = soup.find("div", {"class": "search_news_box"})
    search_newses = search_news_box.find_all(
        "dl", {"class": "search_news"})[0:5]

    for search_news in search_newses:
        link = search_news.find("a")["href"]
        news_name = search_news.find("dt").find("a").getText().strip()
        news_content = search_news.find(
            "dd", {"class": "desc"}).getText().strip()
        news_box = {}
        news_box['title'] = news_name
        news_box['content'] = news_content
        news_box['link'] = link
        chosun.append(news_box)


def donga_scrapper(search_term):
    donga_url = f"http://www.donga.com/news/search?check_news=1&more=1&sorting=1&range=1&search_date=&query={search_term}"
    request = requests.get(donga_url, headers=headers)
    request.encoding = 'utf-8'
    soup = BeautifulSoup(request.text, "html.parser")

    search_list_box = soup.find("div", {"class": "searchCont"})
    search_list_all = search_list_box.find_all(
        "div", {"class": "searchList"})[0:5]

    for search_list in search_list_all:
        news_title = search_list.find(
            "div", {"class": "t"}).find("a").getText()
        news_content = search_list.find(
            "div", {"class": "t"}).find("p", {"class": "txt"}).find("a").getText()
        link = search_list.find("div", {"class": "t"}).find("a")["href"]
        news_box = {}
        news_box['title'] = news_title
        news_box['content'] = news_content
        news_box['link'] = link
        donga.append(news_box)


def portal_scrapper(search_term):
    db = {}
    joongang_scrapper(search_term)
    chosun_scrapper(search_term)
    donga_scrapper(search_term)
    db['joongang'] = joongang
    db['chosun'] = chosun
    db['donga'] = donga
    return db

# yeonhap_url = f"https://www.yna.co.kr/search/index?query={search_term}&ctype=A"
# request = driver.get(yeonhap_url)
# driver.implicitly_wait(3)
# html = driver.page_source
# soup = BeautifulSoup(html, "html.parser")
# article_list = soup.find("div", {"class": "contents01"}).find(
#     "div", {"id": "article_list"})

# yeonhap_url = f"https://www.yna.co.kr/search/index?query={search_term}"
# request = requests.get(yeonhap_url)
# soup = BeautifulSoup(request.text, "html.parser")
# article_list = soup.find("div", {"id": "article_list"})


# print(article_list)
