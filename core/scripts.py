import requests
from bs4 import BeautifulSoup, SoupStrainer
import re
import datetime
from .models import *



def cut_text(text):
	if len(text) < 420:
		return text
	else:
		for i, character in enumerate(text[420:], start=420):
			if character in {'?', '!', '.'}:
				return text[:i] + ".."
	return text[:500]
	

def get_slotech():
	url = "https://slo-tech.com/novice/arhiv/"
	page = requests.get(url).content
	soup = BeautifulSoup(page, 'html.parser')
	news_items = soup.find_all("div", class_="news_item")
	stories = Story.objects.filter(page="st").order_by("-date")[:5]
	urls = {story.url for story in stories}
	for item in news_items:
		url = item.find("meta", itemprop="mainEntityOfPage")["itemid"]
		if stories.exists() and url in urls:
			break
		title = item.find("a",  itemprop="name").text
		date_str = item.find("time",itemprop="datePublished")['datetime'].replace("T", " ").split("+")[0]
		date = datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')
		summary = cut_text(item.find("div", class_="besediloNovice").text)
		instance = Story(title=title,url=url,date=date,summary=summary, page="st")
		instance.save()

def get_monitor():
	url = "https://www.monitor.si/novice/"
	page = requests.get(url).content
	soup = BeautifulSoup(page, 'html.parser')
	news_items = soup.find_all("li", class_="article")
	stories = Story.objects.filter(page="mn").order_by("-date")[:5]
	urls = {story.url for story in stories}
	for item in news_items:
		item_body = item.find("div", class_="text")
		url = "https://www.monitor.si" + item_body.find("a")["href"]
		if stories.exists() and url in urls:
			break
		title = item_body.find("a").text
		summary = cut_text(item.find("p", class_="uvodnovosti").text)
		date_dirty = item.find("div", class_="info").text
		date_match = re.search(r'(\d+\.\d+\.\d{4})(\s)?(\d+\:\d+)?', date_dirty)
		if date_match.group(3):
			date = datetime.strptime(date_match.group(1)+" "+date_match.group(3), '%d.%m.%Y %H:%M')
			instance = Story(title=title,url=url,date=date,summary=summary, page="mn")
			instance.save()

def get_racunalniske_novice():
	url = "https://racunalniske-novice.com/racunalnistvo-telefonija/"
	page = requests.get(url).content
	soup = BeautifulSoup(page, 'html.parser', parse_only=SoupStrainer("div", id="main_list"))
	stories = Story.objects.filter(page="rn").order_by("-date")[:5]
	urls = {story.url for story in stories}
	news_items = soup.find_all("div", class_="article")[1:]
	for item in news_items:
		title_div = item.find("h3", class_="title").find("a")
		url = title_div['href']
		if stories.exists() and url in urls:
			break
		title = title_div.text
		summary = item.find("div", class_="summary").text
		date = rn_get_date(url)
		instance = Story(title=title, url=url, date=date, summary=summary, page="rn")
		instance.save()

def rn_get_date(url):
	page = requests.get(url).content
	soup = BeautifulSoup(page, 'html.parser', parse_only=SoupStrainer("div", class_="date"))
	date_str = soup.find("div", class_="date").text.strip()
	date = datetime.strptime(date_str, '%d.%m.%Y %H:%M')
	return date

scrappers = {
	"st": get_slotech,
	"mn": get_monitor,
	"rn": get_racunalniske_novice,
}

def get_day_average(count_sum):
	earliest = Story.objects.earliest("date").date
	now = datetime.today()
	return round( count_sum / (now-earliest).days, 1)


def pretty_page(page_name):
	return [full for (short, full) in PAGE_CHOICES if short == page_name][0]