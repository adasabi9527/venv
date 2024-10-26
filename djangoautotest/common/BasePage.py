"""
@File    ：page_base.py
@Author  ：sarah
@Date    ：2023-07-21
@Desc    ：Base类：存放所有Page页面公共操作方法
"""
import pytest
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from datetime import datetime
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from python_utils import logger
import time
from selenium.webdriver.support import expected_conditions as EC

class Base():
    def __init__(self, browser='chrome'):
        if browser == 'chrome':
                self.driver = webdriver.Chrome()
        elif browser == 'firefox':
                self.driver = webdriver.Firefox()
        elif browser == 'edge':
                self.driver = webdriver.Edge()
        else:
            raise ValueError(f"Unsupported browser: {browser}")
        self.driver.implicitly_wait(10)

    @pytest.fixture(scope='function')
    def driver(self):
        # 设置 WebDriver
        self.driver = webdriver.Chrome()
        yield driver
        # 测试用例结束后关闭浏览器
        driver.quit()

    def open_url(self, url):
        self.driver.get(url)

    def close(self):
        self.driver_close()

    def  get_logcat(self):
        logs = self.driver.get_log('browser')
        for log in logs:
            logging.info(log)
    def base_find(self, loc, timeout=10, poll=0.5):
        """
        查找元素
        timeout：超时的时长，一般30S，超时未找到报错
        poll：检测间隔时长，默认0.5s，如果有一闪而逝的提示信息框，修改为0.1s
        """
        return WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_element(*loc))

    def save_screen(self):
        current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        self.driver.save_screenshot(f'/Users/kika/path/to/venv/djangoautotest/photoshot/{current_time}.png')

    def handle_alert(self):
        # 等待 alert 弹窗出现
        alert = self.driver.switch_to.alert
        # 获取弹窗文本
        alert_text = alert.text
        # print(alert_text)
        return alert_text
        # 验证弹窗文本是否符合预期
        # assert expected_text in alert_text, f"Expected text '{expected_text}' not found in alert"
    def find_id(self,id):
        return  self.driver.find_element(By.ID,id)

    def find_xpath(self,xpath):
        return  self.driver.find_element(By.XPATH,xpath)

    def find_css(self,csspath):
        return  self.driver.find_element(By.CSS_SELECTOR,csspath)

    def find_class(self,classname):
        return self.driver.find_element(By.CLASS_NAME,classname)

    def base_input(self, loc, text):
        """输入文本"""
        el = self.base_find(loc)
        el.clear()
        if text is not None:
            el.send_keys(text)
        logging.info(f"{el}输入文本:{text}")

    def base_click(self, loc):
        """点击"""
        self.base_find(loc).click()
        time.sleep(5)
        logging.info(f'点击按钮：{loc}')

    def base_get_text(self, loc):
        """获取当前元素文本"""
        _text = self.base_find(loc).text
        logging.info(f"获取文本：{_text}")
        return _text

    def base_get_title(self):
        """获取当前页title"""
        title = self.driver.title
        logging.info(f"当前页面：{title}")
        return title

    def base_alert_confirm(self):
        """自动确认弹框 以便继续进行后续的测试操作"""
        self.driver.switchTo().alert().accept()

    def base_is_dis(self, loc):
        """查看元素是否可见"""
        state = self.base_find(loc).is_displayed()
        logging.info(f"获取元素可见状态：{state}")
        return state

    def base_keep_press(self, loc, time):
        """保持长按"""
        ActionChains(self.driver).click_and_hold(self.base_find(loc)).perform()
        logging.info(f"长按：{loc}")
        time.sleep(5)
        ActionChains(self.driver).release(self.base_find(loc)).perform()
        logging.info(f"释放：{loc}")

    def base_select(self, loc, text):
        """
        下拉框选择
        :param loc: select标签元素，父类, 不是option
        :param text: 通过显示文本选择
        """
        Select(self.base_find(loc)).select_by_visible_text(text)
        logging.info(f"选择下拉框{loc}的{text}")

    def base_tick_checkbox(self, loc, num):
        """勾选框"""
        checkbox_list = self.base_find(loc)
        action = ActionChains(self.driver)
        for i in range(0, num):
            action.move_to_element(checkbox_list[i])
            action.click(checkbox_list[i]).perform()
            time.sleep()

    def base_invisible_element(self, loc, num, stop):
        """对动态变化元素执行动作链"""
        msg = self.base_find(loc)
        for i in range(0, num):
            action = ActionChains(self.driver)
            action.move_to_element(msg[i])
            action.click(msg[i])
            action.perform()
            time.sleep(stop)

    def base_refresh(self):
        """刷新页面F5"""
        self.driver.refresh()
    # 执行完毕关闭
    def driver_close(self):
        self.driver.quit()


