from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class Login:

    def __init__(self, browser, url):
        self.__browser = browser
        self.__url = url
        self.__browser.get(self.__url)
        self.__LOGIN_PAGE = ("arguments[0].click();",self.__browser.find_element(By.XPATH, "//a[@class=\"nav-action-button\"]"))
        self.__EMAIL_FIELD = (EC.element_to_be_clickable((By.XPATH, "//input[@id=\"ap_email\"][@class=\"a-input-text a-span12 auth-autofocus auth-required-field\"]")))
        self.__PASSWORD_FIELD = (EC.element_to_be_clickable((By.XPATH, "//input[@id=\"ap_password\"][@name=\"password\"]")))
        self.__CONTINUE_BUTTON = (By.XPATH, "//input[@id=\"continue\"][@class=\"a-button-input\"]")
        self.__SUBMIT_BUTTON = (By.XPATH, "//input[@id=\"signInSubmit\"][@class=\"a-button-input\"]")


    def login_account(self, email, password):

        wait = WebDriverWait(self.__browser, 10, 1)

        self.__browser.execute_script(*self.__LOGIN_PAGE)
        email_account = wait.until(self.__EMAIL_FIELD)
        email_account.clear()
        email_account.send_keys(email)
        self.__browser.find_element(*self.__CONTINUE_BUTTON).click()

        password_account = wait.until(self.__PASSWORD_FIELD)
        password_account.clear()
        password_account.send_keys(password)
        self.__browser.implicitly_wait(10)
        self.__browser.find_element(*self.__SUBMIT_BUTTON).click()

    

