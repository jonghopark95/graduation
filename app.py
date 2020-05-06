from flask import Flask, render_template, request
from ranking_items import get_ranking_item
from news_portal_scrapper import portal_scrapper

items = get_ranking_item('2020', '05', '06', '15', '20')

print(items[2])
print(portal_scrapper(items[2]))

app = Flask("Graduation Project")


@app.route("/")
def home():
    return render_template("home.html", items=items)


@app.route("/search")
def search():
    return render_template("search.html")
