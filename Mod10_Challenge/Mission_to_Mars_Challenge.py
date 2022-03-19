#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd


# In[ ]:


executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[ ]:


# Visit the mars nasa news site
# search for elements with a specific combination of tag (div) and attribute (list_text)
# telling our browser to wait one second before searching for components
url = 'https://redplanetscience.com'
browser.visit(url)
# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)


# In[ ]:


# set up HTML parser

# The . is used for selecting classes such as list_text,
# so the code 'div.list_text' pinpoints the <div /> tag with the class of list_text

html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('div.list_text')


# In[ ]:


# Begin scraping

slide_elem.find('div', class_='content_title')

# We chain .find onto our previously assigned variable, slide_elem. 
# When we do this, we're saying, "This variable holds a ton of information, 
# so look inside of that information to find this specific data."


# In[ ]:


# Use the parent element to find the first `a` tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title


# In[ ]:


# There are two methods used to find tags and attributes with BeautifulSoup:

    # .find() 
        # used when we want only the first class and attribute we've specified.
        
    # .find_all() 
        # used when we want to retrieve all of the tags and attributes.

# For example, if we were to use .find_all() instead of .find() when pulling the summary, 
# we would retrieve all of the summaries on the page instead of just the first one.


# In[ ]:


# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# # 10.3.4
# # use markdown to separate the article scraping from the image scraping.
# 
# ### Featured Images

# In[ ]:


# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)


# In[ ]:


# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# In[ ]:


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')


# In[ ]:


# Find the relative image url

img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')

    # img tag is nested in HTML
    # .get('src') pulls the link to the image

img_url_rel


# In[ ]:


# Use the base URL to create an absolute URL
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


# In[ ]:


# 10.3.5 SCRAPING TABLES
# Instead of scraping each row, or the data in each <td />, 
# we're going to scrape the entire table with Pandas' .read_html() function.

df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.columns=['description', 'Mars', 'Earth']
df.set_index('description', inplace=True)

    # The Pandas function read_html() specifically searches for and returns a list of tables found in the HTML.
    # By using the .set_index() function, we're turning the Description column into the DataFrame's index.
    
df


# In[ ]:


# Pandas also has a way to easily convert our DataFrame back 
# into HTML-ready code using the .to_html() function. 

df.to_html()


# In[ ]:


# browser.quit()


# In[ ]:





# In[2]:


# Import Splinter, BeautifulSoup, and Pandas
from splinter import Browser
from bs4 import BeautifulSoup as soup
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager


# In[3]:


# Set the executable path and initialize Splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# ### Visit the NASA Mars News Site

# In[4]:


# Visit the mars nasa news site
url = 'https://redplanetscience.com/'
browser.visit(url)

# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)


# In[5]:


# Convert the browser html to a soup object and then quit the browser
html = browser.html
news_soup = soup(html, 'html.parser')

slide_elem = news_soup.select_one('div.list_text')


# In[6]:


slide_elem.find('div', class_='content_title')


# In[7]:


# Use the parent element to find the first a tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title


# In[8]:


# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# ### JPL Space Images Featured Image

# In[9]:


# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)


# In[10]:


# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# In[11]:


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')
img_soup


# In[12]:


# find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel


# In[13]:


# Use the base url to create an absolute url
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


# ### Mars Facts

# In[14]:


df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.head()


# In[15]:


df.columns=['Description', 'Mars', 'Earth']
df.set_index('Description', inplace=True)
df


# In[16]:


df.to_html()


# # D1: Scrape High-Resolution Mars’ Hemisphere Images and Titles

# ### Hemispheres

# In[17]:


# 1. Use browser to visit the URL 
url = 'https://marshemispheres.com/'

browser.visit(url)


# In[18]:


# 2. Create a list to hold the images and titles.
hemisphere_image_urls = []

# 3. Write code to retrieve the image urls and titles for each hemisphere.
for pics in range(0, 4):

    full_image_elem = browser.find_by_tag('h3')[pics]
    full_image_elem.click()
    
    html = browser.html
    
    img_soup = soup(html, 'html.parser')
    img_soup
    img_url_rel = img_soup.find('img', class_= 'wide-image').get('src')
    img_url = f'{url}{img_url_rel}'
    title = img_soup.find('h2').text
    
    #Clicks Back Button to Return to Main Homepage
    full_image_elem = browser.find_by_tag('h3')[1]
    full_image_elem.click()
    
    hemisphere_dict= {'title': title, 'img_url': img_url}
    hemisphere_image_urls.append(hemisphere_dict)     


# In[19]:


# 4. Print the list that holds the dictionary of each image url and title.
hemisphere_image_urls


# In[20]:


# 5. Quit the browser
browser.quit()


# In[ ]:





# In[ ]:




