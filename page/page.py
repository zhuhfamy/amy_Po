from page.dx_input_ele import DxInput
from page.dx_nuw_click import DxNuw


class Page:

    def __init__(self, driver):
        self.driver = driver

    @property
    def new_click(self):
        return DxNuw(self.driver)

    @property
    def input_ele(self):
        return DxInput(self.driver)