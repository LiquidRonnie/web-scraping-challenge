# Load dependencies
from bs4 import BeautifulSoup
from splinter import Browser
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager


def scrape_info():

    ################ MARS NEWS ####################################

    # Set the executable path and initialize the chrome browser in splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    # Vist URL
    url = "https://redplanetscience.com/"
    browser.visit(url)

    # Convert the browser html to a soup object
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    # Obtain New Title
    news_title = soup.find_all(class_="content_title")[0].get_text()
    news_title

    # Obtain news paragraph
    paragraph_text = soup.find_all(class_="article_teaser_body")[0].get_text()
    paragraph_text

    ##################################################################

    ###### JPL Mars Spaces Images ########################

    # Vist URL
    url = 'https://spaceimages-mars.com/'
    browser.visit(url)

    # Convert the browser html to a soup object
    mars_images = browser.html
    soup = BeautifulSoup(mars_images, 'html.parser')

    # assign variable to URL
    featured_image_url = url + soup.find('a', class_='showimg fancybox-thumbs')['href']
    print(featured_image_url)


    #  # Mars Image
    # mars_img_url = 'https://spaceimages-mars.com/'
    # browser.visit(mars_img_url)
    # mars_img_html = browser.html
    # mars_img_soup = BeautifulSoup(mars_img_html, 'html.parser')
    # featured_image_url = mars_img_url + mars_img_soup.find('a', class_='showimg fancybox-thumbs')['href']
    # print(featured_image_url)


    ######################################################

    ###################### MARS FACTS ##########################

    # use Pandas to scrape the table containing facts about the planet  
    mars_df = pd.read_html("https://galaxyfacts-mars.com/")[0]
    #mars_df

    # Rename columns and remove first row
    mars_df = mars_df.rename(columns={0:"Description", 1:"Mars", 1:"Mars", 2:"Earth"})
    mars_df = mars_df.drop(mars_df.index[0])
    #mars_df


    # Set Description as index
    mars_df.set_index("Description", inplace=True)

    # Use Pandas to convert the data to a HTML table string
    mars_facts = mars_df.to_html()

    mars_facts.replace('\n','')

    ##############################################################

    #################### MARS HEMISPHERES ##############################

    # Vist URL
    url = "https://marshemispheres.com/"
    browser.visit(url)

    # Convert the browser html to a soup object
    hem = browser.html
    soup = BeautifulSoup(hem, 'html.parser')

    # find titles
    title = soup.find_all('div', class_='description')

    titles = []
    # Being for loop to git titles
    for title in title:
        titles.append(title.find('h3').text.strip())

    #####################################################################

    ################### Hemispheres  #####################################

    ######################## CERBERUS #####################################

    # create empty list
    hemispheres = []

    # create URL variables 
    base_url = "https://marshemispheres.com/"
    url = "https://marshemispheres.com/cerberus.html"

    # visit URL
    browser.visit(url)

    hem = browser.html
    # Parse HTML with Beautiful Soup
    soup = BeautifulSoup(hem, 'html.parser')
    # Retrieve all elements that contain book information
    Cerberus = base_url + soup.find('div', class_='downloads').a['href']
    
    hemispheres.append(Cerberus)
    #Cerberus


    ######################## schiaparelli #####################################

    base_url = "https://marshemispheres.com/"
    url = "https://marshemispheres.com/schiaparelli.html"


    browser.visit(url)

    hem = browser.html
    # Parse HTML with Beautiful Soup
    soup = BeautifulSoup(hem, 'html.parser')
    # Retrieve all elements that contain book information
    schiaparelli = base_url + soup.find('div', class_='downloads').a['href']

    hemispheres.append(schiaparelli)

    ######################## syrtis #####################################

    base_url = "https://marshemispheres.com/"
    url = "https://marshemispheres.com/syrtis.html"

    browser.visit(url)

    hem = browser.html
    # Parse HTML with Beautiful Soup
    soup = BeautifulSoup(hem, 'html.parser')
    # Retrieve all elements that contain book information
    syrtis = base_url + soup.find('div', class_='downloads').a['href']
    syrtis

    hemispheres.append(syrtis)
    syrtis

    
    ######################## Valles #####################################

    base_url = "https://marshemispheres.com/"
    url = "https://marshemispheres.com/valles.html"


    browser.visit(url)

    hem = browser.html
    # Parse HTML with Beautiful Soup
    soup = BeautifulSoup(hem, 'html.parser')
    # Retrieve all elements that contain book information
    valles = base_url + soup.find('div', class_='downloads').a['href']
    
    hemispheres.append(valles)
    
    hem_list = [
    {"title":titles[0], "img_url":hemispheres[0]},
    {"title":titles[1], "img_url":hemispheres[1]},
    {"title":titles[2], "img_url":hemispheres[2]},
    {"title":titles[3], "img_url":hemispheres[3]}
    ]

    #####################################################################
    #####################################################################

    mars_dict = {
        "news_title": news_title,
        "paragraph_text": paragraph_text,
        "featured_image_url": featured_image_url,
        "mars_facts": mars_facts,
        "hem_list": hem_list,
    }

    # Close the browser after scraping
    browser.quit()

    # Return results
    return mars_dict
