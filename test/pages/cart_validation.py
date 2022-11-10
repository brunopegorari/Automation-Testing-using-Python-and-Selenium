from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from add_cart import AddCart


class CartValidation():

    def __init__(self, browser):
        self.__browser = browser

    def item_title(self):
        title = self.__browser.find_element(By.XPATH, "//span[@class=\"a-truncate-cut\"]")
        return title
    
    def item_author(self):
        author = self.__browser.find_element(By.CLASS_NAME, "a-size-base sc-product-creator")
        return author
    
    def item_price(self):
        price = self.__browser.find_element(By.XPATH, "//span[@class=\"a-size-medium a-color-base sc-price sc-white-space-nowrap sc-product-price a-text-bold\"]")
        return price

    def item_subtotal_1(self):
        subtotal_1 = self.__browser.find_element(By.XPATH, "//span[@class=\"a-size-medium a-color-base sc-price sc-white-space-nowrap\"]")
        return subtotal_1
    
    def item_subtotal_2(self):
        subtotal_2 = self.__browser.find_element(By.XPATH, "//span[@id=\"sc-subtotal-amount-buybox\"]")
        return subtotal_2

    def cart_informations_validation(self, title_name, author_name, price_item, get_author):
        title = item_title()
        author = item_author()
        price = item_price()
        subtotal_1 = item_subtotal_1()
        subtotal_2 = item_subtotal_2()
        

        assert title_name in title.text
        assert author_name in author.text
        assert price_item in price.text
        assert price_item in subtotal_1.text
        assert price_item in subtotal_2.text         
        
    
