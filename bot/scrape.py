from bs4 import BeautifulSoup
import requests, lxml

def make_request(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "lxml")
    return soup

def get_active_cases():
    soup = make_request("https://www.worldometers.info/coronavirus/")
    value = soup.find("div", class_="number-table-main")
    print(value.text)

def get_new_updates(country):
    soup = make_request(f"https://www.worldometers.info/coronavirus/country/{country}/")
    value = soup.find("li", class_="news_li")
    if "[source]" in value.text:
        value = value.text.replace("[source]", "")
    print(value)

get_new_updates("germany")