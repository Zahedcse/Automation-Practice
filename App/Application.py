from Pages.Login import Login


class Application:
    def __init__(self, driver):
        self.driver = driver
        self.login_page = Login(self.driver)
