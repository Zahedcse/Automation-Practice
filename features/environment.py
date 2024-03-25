import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from App.Application import Application


def browser_init(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.implicitly_wait(10)
    context.driver.wait = WebDriverWait(context.driver, 10)
    context.app = Application(context.driver)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context)


def after_scenario(context):
    # context.driver.delete_all_cookies()
    context.driver.quit()


def after_step(context, step):
    if step.status == 'failed':
        allure.attach(context.driver.get_screenshot_as_png()
                      , name="failed_screenshot"
                      , attachment_type=AttachmentType.PNG)
