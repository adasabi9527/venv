from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoAlertPresentException


class AlertHandler:
    def __init__(self, driver):
        self.driver = driver

    def handle_alert(self, expected_text, accept=True):
        """
        处理 alert 弹窗的方法。

        :param expected_text: 期望在 alert 弹窗中显示的文本。
        :param accept: 是否接受弹窗，默认为 True。
        """
        try:
            # 等待 alert 弹窗出现
            alert = WebDriverWait(self.driver, 10).until(EC.alert_is_present())

            # 获取弹窗文本
            alert_text = alert.text

            # 验证弹窗文本是否符合预期
            assert expected_text in alert_text, f"Expected text '{expected_text}' not found in alert"

            # 根据参数决定是接受还是拒绝弹窗
            if accept:
                alert.accept()
            else:
                alert.dismiss()

        except NoAlertPresentException:
            print("No alert is present.")
        except AssertionError as e:
            print(e)
        except Exception as e:
            print(f"An error occurred: {e}")