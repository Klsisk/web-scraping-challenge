#Dependencies
from splinter import Browser
from bs4 import BeautifulSoup as bs
import pandas as pd
import requests

def init_browser():
    #Choose the executable path to driver 
    path = 'chromedriver.exe'
    return Browser('chrome', executable_path=path, headless=False)

## MARS DATA FROM VARIOUS WEBSITES ##
def scrape():
    # Initialize browser 
    browser = init_browser()
    mars_data = {}
    
    
    #Visit Nasa News site 
    url = 'https://mars.nasa.gov/news'
    browser.visit(url)
   

    # Scrape page into Soup
    html = browser.html
    soup = bs(html, 'html.parser')

    #Retrieve news title
    article = soup.find('div', class_="list_text")
    news_title= article.find('div', class_="content_title").text
    mars_data['news_title'] = news_title

    #Retrieve news paragraph
    news_p = article.find('div', class_="article_teaser_body").text
    mars_data['news_p'] = news_p

    ## JPL Mars Space Images - Featured Image ##
    #Go to the JPL Mars Space Images through the splinter module
    img_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(img_url)

    #Find and click the full image button
    full_image_elem = browser.find_by_id('full_image')
    full_image_elem.click()

    #Find the more info button and click that
    browser.is_element_present_by_text('more info', wait_time=1)
    more_info_elem = browser.links.find_by_partial_text('more info')
    more_info_elem.click()

    #Parse the resulting html with soup
    html = browser.html
    img_soup = bs(html, 'html.parser')

    #Find the relative image url
    image_url = img_soup.select_one('figure.lede a img').get("src")

    #Use the base url to create an absolute url
    featured_image_url = f'https://www.jpl.nasa.gov{image_url}'
    mars_data['featured_image_url'] = featured_image_url
    
    
    
    ## Mars Facts ##
    #Go to the Mars Facts url
    mars_url = 'https://space-facts.com/mars/'

    #Use Panda's `read_html` to parse the url
    tables = pd.read_html(mars_url, index_col=None)

    #Want to use table with Diameter and Mass which would be index 0
    df = tables[0]

    #Assign the columns `['Description', 'Value']`
    df.columns = ['Description', 'Value']

    #Set the index to the `Description` column
    df.set_index('Description', inplace=True)

    #Use 'to_html' method to generate HTML tables from DataFrames
    html_table = df.to_html()

    #Strip unwanted newlines to clean up the table
    html_table.replace('\n', '')
    mars_data['mars_facts_table'] = html_table



    ## Mars Hemispheres ##
    #Go to USGS Astrogeology site splinter module
    hemisphere_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(hemisphere_url)

    #Create BeautifulSoup object; parse with 'html.parser'
    hemisphere_html = browser.html
    soup = bs(hemisphere_html, 'html.parser')

    hemisphere_image_urls = []

    #First, get a list of all of the hemispheres
    links = browser.find_by_css("a.product-item h3")

    #Next, loop through those links, click the link, find the sample anchor, return the href
    for i in range(len(links)):
        hemisphere = {}
    
        #We have to find the elements on each loop to avoid a stale element exception
        browser.find_by_css("a.product-item h3")[i].click()
    
        #Next, we find the Sample image anchor tag and extract the href
        sample_elem = browser.links.find_by_text('Sample').first
        hemisphere['img_url'] = sample_elem['href']
    
        #Get Hemisphere title
        hemisphere['title'] = browser.find_by_css("h2.title").text
    
        #Append hemisphere object to list
        hemisphere_image_urls.append(hemisphere)

        #Finally, we navigate backwards
        browser.back()
        mars_data['hemisphere_image_urls'] = hemisphere_image_urls

    #Quite the browser after scraping
    browser.quit()

    print(mars_data)

    #Return results
    return mars_data
    

   