from selenium.webdriver.common.by import By


class BookSeacher:

    def __init__(self, browser):
        self.__browser = browser
        self.__SEARCHER_BAR= (By.ID, "twotabsearchtextbox")
        self.__GO_BUTTON = (By.XPATH, "//input[@id=\"nav-search-submit-button\"][@value=\"Ir\"]")
        
    def item_seacher(self, item):

        searching = self.__browser.find_element(*self.__SEARCHER_BAR)
        searching.clear()
        searching.send_keys(item)
        self.__browser.find_element(*self.__GO_BUTTON).click()
        self.__browser.find_element(By.LINK_TEXT, item).click()
    

    


