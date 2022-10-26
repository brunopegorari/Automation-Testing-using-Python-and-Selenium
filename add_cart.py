from selenium.webdriver.common.by import By

class AddCart:
    
    def __init__(self, browser):
        self.__browser = browser
        self.__PRODUCT_TITLE = (By.XPATH, "//span[@id=\"productTitle\"][@class=\"a-size-extra-large\"]")
        self.__AUTHOR_NAME = (By.CLASS_NAME, "a-link-normal contributorNameID") #ARRUMAR ESSE PONTO!!!!!!!!!!!!!!!!!!!!!!
        self.__PRICE = (By.ID, "price")
        self.__ADD_CART = (By.XPATH, "//input[@id=\"add-to-cart-button\"][@class=\"a-button-input\"]")
        self.__GO_TO_CART = (By.LINK_TEXT, "Ir para o carrinho")

    def item_product_tile(self):
        item_title = self.__browser.find_element(*self.__PRODUCT_TITLE)
        return item_title 

    def item_author_name(self):
        author = self.__browser.find_element(*self.__AUTHOR_NAME)
        return author

    def item_price(self):
        price = self.__browser.find_element(*self.__PRICE)
        return price

    def add_to_cart(self):
        self.__browser.find_element(self.__ADD_CART)
        self.__browser.find_element(self.__GO_TO_CART)


    def itens_validations(self, title_name, author_name, price_item):
        title = self.item_product_tile()
        author = self.item_author_name()
        price = self.item_price()
        
        assert title_name in title.text
        assert author_name in author.text
        assert price_item in price.text 
        
    
