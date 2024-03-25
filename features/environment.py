import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from App.Application import Application


def browser_init(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.implicitly_wait(10)
    context.driver.wait = WebDriverWait(context.driver)
    context.app = Application(context.driver)


def before_scenario(self, scenario):
    print('\n Started Scenario: ', scenario.name)
    browser_init(context)


def after_step(self, step):
    if step.status == 'failed':
        allure.attach(context.driver.get_screenshot_as_png(), name='failed screenshot', attachment_type=AttachmentType.PNG)
