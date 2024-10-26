import time
import pytest
import logging
import allure
import urllib3
from datetime import  datetime
from selenium import webdriver
from djangoautotest.common import BasePage
from djangoautotest.data.login_data import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from djangoautotest.common.AutoSaveLog import AutoSaveLogger
current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
url= 'http://127.0.0.1:9999/admin/login/?next=/admin/'
driver = BasePage.Base(browser='chrome')

logging.info("开始执行测试用例：test_login")

@pytest.fixture(scope="function")
def logger_fixture():
    logger = AutoSaveLogger(f"/Users/kika/path/to/venv/djangoautotest/log/{current_time}.log")
    yield logger.get_logger()
    logger.close_logger()

@pytest.mark.login
# 参数化数据
@pytest.mark.parametrize("logindict", [cases_success])
@allure.description("测试用户登录功能，预期用户能够成功登录系统。")
@pytest.mark.flaky(retries=1, delay=1)
def test_login(logindict):
    driver.open_url(url)

    account = logindict["account"]
    password = logindict["password"]
    expected = logindict["expected"]
    login_input = driver.find_id('id_username').send_keys(account)
    pwd_input = driver.find_id('id_password').send_keys(password)
    sub_input= driver.find_xpath('//*[@id="login-form"]/div[3]/input').click()
    ui_content= driver.find_id('user-tools').text
    assert expected in ui_content
    back_to_login = driver.find_xpath('//*[@id="logout-form"]/button').click()
    click_login_again = driver.find_xpath('//*[@id="content"]/p[2]/a').click()
    logging.info('')
    driver.save_screen()

@pytest.mark.error
@allure.description("测试用户登录功能，预期用户登陆失败。")
@pytest.mark.parametrize("logindicterror1", [cases_error1])
@pytest.mark.flaky(retries=1, delay=1)
def test_login_wracpwd(logindicterror1):
    driver.open_url(url)
    account1 = logindicterror1["account1"]
    password1 = logindicterror1["password1"]
    expected1 = logindicterror1["expected1"]
    login_input = driver.find_id('id_username').send_keys(account1)
    pwd_input = driver.find_id('id_password').send_keys(password1)
    sub_input = driver.find_xpath('//*[@id="login-form"]/div[3]/input').click()
    ui_content = driver.find_xpath('//*[@id="content"]/p').text
    assert expected1 in ui_content

    time.sleep(5)
    driver.save_screen()

@pytest.mark.error
@allure.description("测试用户登录功能，预期用户登陆失败。")
@pytest.mark.parametrize("logindicterror2", [case_error2])
def test_login_wracpwd1(logindicterror2):
    driver.open_url(url)
    account2 = logindicterror2["account2"]
    password2 = logindicterror2["password2"]
    expected2 = logindicterror2["expected2"]
    login_input = driver.find_id('id_username').send_keys(account2)
    pwd_input = driver.find_id('id_password').send_keys(password2)
    sub_input = driver.find_xpath('//*[@id="login-form"]/div[3]/input').click()
    ui_content = driver.find_xpath('//*[@id="content"]/p').text
    assert expected2 in ui_content

    time.sleep(5)
    driver.save_screen()
    driver.driver_close()
logging.info("执行测试用例：test_login结束")
# @pytest.mark.parametrize("logindicterror3", [case_error3])
# def test_login_wracpwd2(logindicterror3):
#     driver.open_url(url)
#     account3 = logindicterror3["account3"]
#     password3 = logindicterror3["password3"]
#     expected3 = logindicterror3["expected3"]
#     login_input = driver.find_id('id_username').send_keys(account3)
#     pwd_input = driver.find_id('id_password').send_keys(password3)
#     sub_input = driver.find_xpath('//*[@id="login-form"]/div[3]/input').click()
#     alert_content = driver.handle_alert()
#     assert expected3 in alert_content
#     driver.save_screen()
#     driver.base_quit()







