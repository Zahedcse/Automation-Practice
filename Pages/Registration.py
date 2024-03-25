from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from Pages.utilities import Page


class Registration(Page):
    HomePage = (By.XPATH, "//a[normalize-space()='Home']")
    signup = (By.LINK_TEXT, 'Signup / Login')
    new_user_signup_text = (By.XPATH, "//div[@class='signup-form']//h2[1]")
    # Register Data
    name = (By.NAME, "name")
    Email_address = (By.XPATH, "(//input[@name='email'])[2]")
    submit = (By.XPATH, "(//button[@class='btn btn-default'])[2]")

    # Account Information
    Account_information = (By.XPATH, "(//h2[@class='title text-center']//b)[1]")
    Title = (By.ID, "id_gender1")
    Password = (By.ID, "password")
    Day = (By.ID, "days")
    Months = (By.ID, "months")
    Years = (By.ID, "years")
    Newsletter = (By.ID, "newsletter")
    Special_offer = (By.ID, "optin")

    # Fill Details
    First_Name = (By.ID, "first_name")
    Last_Name = (By.ID, "last_name")
    Company = (By.ID, "company")
    Address = (By.ID, "address1")
    # Country = Select(By.NAME, "country")
    # Country.select_by_value("India")
    State = (By.ID, "state")
    Zipcode = (By.ID, "zipcode")
    Mobile_Number = (By.ID, "mobile_number")
    Submit = (By.XPATH, "(//button[@class='btn btn-default'])[1]")

    # Check Account Creation
    AccountCreation = (By.TAG_NAME, "b")
    Continue = (By.LINK_TEXT, "Continue")
    LoggedInAsUserName = (By.TAG_NAME, "b")
    Delete_Account = (By.LINK_TEXT, "Delete Account")
    Account_Deleted = (By.TAG_NAME, "b")
    Continue_Button = (By.LINK_TEXT, "Continue")

    def NavigateToURL(self):
        self.open_page('https://automationexercise.com/')
