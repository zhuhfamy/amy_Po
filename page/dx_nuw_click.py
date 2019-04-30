from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class DxNuw(BaseAction):

    # 点击新增短信
    dx_new_click = By.ID, "com.android.mms:id/action_compose_new"

    def page_dx(self):
        self.click(self.dx_new_click)
