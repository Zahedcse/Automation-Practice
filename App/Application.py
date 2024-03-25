from Pages.Registration import Registration


class Application:
    def __init__(self, driver):
        self.driver = driver
        self.reg_page = Registration(self.driver)
