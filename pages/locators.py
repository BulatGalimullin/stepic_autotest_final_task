from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    CARD_LINK = (By.CSS_SELECTOR, 'a[class="btn btn-default"]')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")
    REGISTRATION_EMAIL = (By.NAME, "registration-email")
    REGISTRATION_PASSWORD = (By.NAME, "registration-password1")
    REGISTRATION_PASSWORD_CONFIRM = (By.NAME, "registration-password2")
    REGISTER_BUTTON = (By.NAME, "registration_submit")


class ProductPageLocators:
    ADD_TO_CARD_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")
    REVIEW_BUTTON = (By.ID, "write_review")
    TOTAL_BASKET_PRICE = (By.CSS_SELECTOR, 'div.alertinner  > p > strong')
    PRODUCT_PRICE = (By.CSS_SELECTOR, "p.price_color")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.col-sm-6 > h1")
    PRODUCT_NAME_MESSAGE = (By.CSS_SELECTOR, "div#messages > :nth-child(1) > div > strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div#messages > :nth-child(1)")


class BasketPageLocators:
    CHECKOUT_LINK = (By.CSS_SELECTOR, "[class='btn btn-lg btn-primary btn-block']")
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, "div#content_inner > p")
