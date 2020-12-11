import pandas as pd
from splinter import Browser
from bs4 import BeautifulSoup as bs
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager 

#set up  chromedriver
def init_browser():
    executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    browser = Browser("chrome", **executable_path, headless=False)
    return browser

#open the chrome website 
mars_website_info = {}

def scrape():
    browser = init_browser()

    # opening the url 
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)
    time.sleep(1)

    html = browser.html
    soup = bs(html, 'html.parser')

#scrape and print most recent article on website
    all_articles = soup.find('ul', class_='item_list')
    first_article = all_articles.find('li', class_='slide')

#set variables
    news_title = first_article.find('div', class_='content_title').text
    news_p = first_article.find('div', class_='article_teaser_body').text
    mars_website_info["news_title"] = news_title
    mars_website_info["news_p"] = news_p

    return mars_website_info

##JPL MARS SPACE IMAGES

def image_main_scrape():
    # visit the JPL website and scrape the main image
    images_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser = init_browser()
    images_visit = browser.visit(images_url)
    time.sleep(1)

    images_visit.click_link_by_partial_text('FULL IMAGE')
    time.sleep(1)

    expand = images_visit.find_by_css('a.fancybox-expand')
    expand.click()
    time.sleep(1)

    jpl_html = images_visit.html
    jpl_soup = bs(jpl_html, 'html.parser')

    image_search = jpl_soup.find('img', class_='fancybox-image')['src']
    image_path = f'https://www.jpl.nasa.gov{image_search}'
    mars_website_info["image_path"] = image_path
  
##MARS FACTS
def mars_facts():
     # Visit the Mars Facts webpage
    facts_url = 'https://space-facts.com/mars/'
    planet_facts = pd.read_html(facts_url)

    #pull info into data frame
    mars_info = planet_facts[0]
    mars_info.columns = ['Description', 'Value']
  
    #set to HTML 
    mars_facts_html = mars_info.to_html(header=False, index=False)
    mars_website_info['planet_facts'] = mars_facts_html

    return mars_website_info






