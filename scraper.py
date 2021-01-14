import mail
import requests
from bs4 import BeautifulSoup

agent = {"user-agent": "Mozilla/5.0 (X11; Linux i686; rv:84.0) Gecko/20100101 Firefox/84.0"}


def check_stock():
    page = requests.get(mail.URL, headers=agent)
    soup = BeautifulSoup(page.content, 'html.parser')

    try:
        return soup.find('button', string="Sold Out").string == "Sold Out"
    except:
        return False


def get_product_name(URL):
    page = requests.get(URL, headers=agent)
    soup = BeautifulSoup(page.content, 'html.parser')

    return soup.find(class_="heading-5 v-fw-regular").string
