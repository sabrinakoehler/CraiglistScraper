from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

from bs4 import BeautifulSoup
import urllib.request

class CraiglistScaper(object):
    """This is a class for scraping Craiglist postings for bicycles given certain specifications of what to search for"""
    def __init__(self, location, postal, max_price, radius, bike, brakes, handlebars):
        """The constructor for CraiglistScraper class"""
        self.location = location
        self.postal = postal
        self.max_price = max_price
        self.radius = radius
        self.bike = bike
        self.brakes = brakes
        self.handlebars = handlebars

        self.url = f"https://{location}.craigslist.org/search/sss?search_distance={radius}&postal={postal}&max_price={max_price}&bicycle_type={bike}&bicycle_brake_type={bicycle_brake_type}&bicycle_handlebar_type={bicycle_handlebar_type}"

        self.driver = webdriver.Chrome()
        self.delay = 3

    def load_craigslist_url(self):
        """The function to load the Craiglist results page in Chrome browser"""
        self.driver.get(self.url)
        try:
            wait = WebDriverWait(self.driver, self.delay)
            wait.until(EC.presence_of_element_located((By.ID, "searchform")))
            print("Page is ready")
        except TimeoutException:
            print("Loading took too much time")

    def extract_post_titles(self):
        """The function to print out Craiglist post titles in Terminal"""
        all_posts = self.driver.find_elements_by_class_name("result-row")
        post_title_list = []
        for post in all_posts:
            print(post.text)
            post_title_list.append(post.text)
        return post_title_list

    def extract_post_urls(self):
        """The function to print out Craiglist post urls in Terminal"""
        url_list = []
        html_page = urllib.request.urlopen(self.url)
        soup = BeautifulSoup(html_page, "html.parser")
        for link in soup.findAll("a", {"class": "result-title hdrlnk"}):
            print(link["href"])
            url_list.append(link["href"])
        return url_list

    def quit(self):
        """The function to close browser window if desired after running program"""
        self.driver.close()

location = "philadelphia"
postal = "19460"
max_price = "1200"
radius = "100"
bicycle_type = "4"
bicycle_brake_type = "5"
bicycle_handlebar_type = "6"

scraper = CraiglistScaper(location, postal, max_price, radius, bicycle_type, bicycle_brake_type, bicycle_handlebar_type)
scraper.load_craigslist_url()
scraper.extract_post_titles()
scraper.extract_post_urls()
#scraper.quit()