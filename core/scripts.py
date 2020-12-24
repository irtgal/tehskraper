import requests
from bs4 import BeautifulSoup
import re
import datetime
from .models import *

def get_slotech():
	url = "https://slo-tech.com/novice/arhiv/"
	page = requests.get(url).content
	soup = BeautifulSoup(page, 'html.parser')
	news_items = soup.find_all("div", class_="news_item")
	stories = Story.objects.filter(page="st").order_by("-date")[:5]
	titles = [story.title for story in stories]
	for item in news_items:
		title = item.find("a",  itemprop="name").text
		if stories.exists() and title in titles:
			break
		href = item.find("meta", itemprop="mainEntityOfPage")["itemid"]
		date_str = item.find("time",itemprop="datePublished")['datetime'].replace("T", " ").split("+")[0]
		date = datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')
		summary = item.find("div", class_="besediloNovice").text
		instance = Story(title=title,slug=href,date=date,summary=summary, page="st")
		instance.save()

def get_monitor():
	url = "https://www.monitor.si/novice/"
	page = requests.get(url).content
	soup = BeautifulSoup(page, 'html.parser')
	news_items = soup.find_all("li", class_="article")
	stories = Story.objects.filter(page="mn").order_by("-date")[:5]
	titles = [story.title for story in stories]
	for item in news_items:
		item_body = item.find("div", class_="text")
		title = item_body.find("a").text
		if stories.exists() and title in titles:
			break
		href = "https://www.monitor.si" + item_body.find("a")["href"]
		summary = item.find("p", class_="uvodnovosti").text
		date_dirty = item.find("div", class_="info").text
		date_str = re.findall(r'\d+\.\d+\.\d{4}\s+\d+\:\d+', date_dirty)[0]
		date = datetime.strptime(date_str, '%d.%m.%Y %H:%M')
		instance = Story(title=title,slug=href,date=date,summary=summary, page="mn")
		instance.save()

