from selenium import webdriver
from pages.login import Login
from pages.book_seacher import BookSeacher
from pages.add_cart import AddCart



browser = webdriver.Firefox()
url = 'https://www.amazon.com.br'

#Login information
email = 'insert a valid email'
password = 'insert a valid password'

#Product information
title = "The Lord of the Rings Boxed Set: The Classic Bestselling Fantasy Novel"
author = "J. R. R. Tolkien"
price = " R$ 1.219,84"

#LOGIN
login_amazon = Login(browser, url)
login_amazon.login_account(email, password)

#SEARCH FOR A ITEM
searching_item = BookSeacher(browser)
searching_item.item_seacher(title)

#Item added to cart
cart =  AddCart(browser)
cart.itens_validations(title, author, price)
cart.add_to_cart()

#Cart







#browser.quit()
