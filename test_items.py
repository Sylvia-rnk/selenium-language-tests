from selenium.webdriver.common.by import By

def test_add_to_cart_button_present(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    add_to_cart_button = browser.find_elements(By.CSS_SELECTOR, "button.btn-add-to-basket")
    assert len(add_to_cart_button)> 0, "Add to cart button is not presenton the page"
    assert add_to_cart_button(0).is_displayed(), "Add to cart button is not visible"
