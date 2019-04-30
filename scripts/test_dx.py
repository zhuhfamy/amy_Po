

from base.base_driver import init_driver
from page.page import Page


class TestDx:
    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def test_dx(self):
        self.page.new_click.page_dx()
        self.page.input_ele.pege_input_name("123")
        self.page.input_ele.pege_input_text("12")
        self.page.input_ele.page_sent()






