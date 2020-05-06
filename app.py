from flask import Flask, render_template, request
from ranking_items import get_ranking_item
from news_portal_scrapper import portal_scrapper

# 원하는 시간이 있다면 해당 시간의 검색어를 크롤링한다.
# 검색 주기는 정하지 않았지만 후에 변경 가능하다.
items = get_ranking_item('2020', '05', '06', '15', '20')

app = Flask("Graduation Project")

# 검색어 순위를 보여주기 위한 간단한 HTML
@app.route("/")
def home():
    return render_template("home.html", items=items)


@app.route("/search")
def search():
    return render_template("search.html")
