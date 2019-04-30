from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class DxInput(BaseAction):

    # 输入接收者
    dx_input_name = By.XPATH, "//*[@text = '接收者']"
    # 输入文本内容
    dx_input_text = By.XPATH, "//*[@text = '键入信息']"
    # 点击发送按钮
    dx_click_btn = By.ID, "com.android.mms:id/send_button_sms"

    def pege_input_name(self, name):
        self.input(self.dx_input_name,name)

    def pege_input_text(self, text):
        self.input(self.dx_input_text,text)
    def page_sent(self):
        self.click(self.dx_click_btn)





