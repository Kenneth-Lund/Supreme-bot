import requests
import time
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select

#Hello! Welcome to this short demo.  I am still new to Python, let me know if you would like a tutorial on this script!

keywords = "You can put any keywords here polo striped"   #put as many keywords as you want, it will autmatically match product still
color = "red"      #this color must match same exact one, (lowercase though)
size = "XSmall"       #you can pick any size, automatically checks for the next size up if out of stock
base_url = "http://www.supremenewyork.com"
size_counter = 0

supreme_sizes = ["XSmall","Small", "Medium", "Large", "XLarge"]





"""
This function will refresh/make a request to website until product is loaded on the page, after loaded
it will then try to add the product created from link
"""

def product_checker(keywords, color, base_url):

    product_link = ''
    #while the product link has not been found, keep searching site
    while (product_link == ''):
        test = False
        print("Searching...")

        data = requests.get("http://www.supremenewyork.com/shop/all/tops_sweaters")
        soup = bs(data.text, "html.parser")

        inner_articles = soup.find_all('div', {'class':'inner-article'})

        for article in inner_articles:

            sold_out_tag = article.find('div', {'class':'sold_out_tag'})

            a_tag = article.find('a')
            href = a_tag.get('href')

            pname = str(article.find('h1').text.lower())
            pcolor = article.find('p').text.lower()

            keywords.split()
            pname.split()

            for x in range(len(keywords)):
                for i in range(len(pname)):
                    if keywords[x] in pname[i]:
                        test = True

            if sold_out_tag == None and test == True and pcolor in color:
                product_link = base_url + href
                print("Product Found!")
                print("\n")
                break

        time.sleep(2)

    return product_link







#adds product to cart based on selected size, if unavailble will check next size up

def add_to_cart(size_counter, size):

    mySelect = Select(browser.find_element_by_id("s"))

    try:
        print("Adding to cart..")
        print("\n")

        mySelect.select_by_visible_text(size)
        xpath1 = '//*[@id="add-remove-buttons"]/input'
        box = browser.find_element_by_xpath(xpath1)
        box.click()
        xpath2 = '//*[@id="cart"]/a[2]'
        check_out_box = browser.find_element_by_xpath(xpath2)
        check_out_box.click()
    except:
        #if size was unavailable we are going to check the next size up 
        size = rotate_size(size_counter, supreme_sizes)
        size_counter += 1
        #execute add to cart with new size
        add_to_cart(size_counter, size)
        browser.refresh()
        time.sleep(1)





#This function checks the next size up in the supreme size list
def rotate_size(size_counter, supreme_sizes):

    if size_counter > 4:
        size_counter = 0
    else:
        next_size = supreme_sizes[size_counter]
        print("size unavailable or Out of Stock trying again...")
        print("Rotating Size to " + next_size)
        print("\n")

    return next_size






product_link = product_checker(keywords, color, base_url)
#get product link

#initialize browser
options = Options()
#options.add_experimental_option("excludeSwitches",["ignore-certificate-errors"])
#options.add_argument('--disable-gpu')
#options.add_argument('--headless')
browser = webdriver.Chrome(options= options, executable_path=r'/Users/KennethLund/Downloads/chromedriver')
browser.get(product_link)

#start trying to add to cart after product link is loaded
add_to_cart(size_counter, size)
print("Product Added Successfully!")







