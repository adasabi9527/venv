import pytest
import allure
import logging
from djangoautotest.common import BasePage
from djangoautotest.data.add_group import *
from djangoautotest.data.login_data import *


url= 'http://127.0.0.1:9999/admin/login/?next=/admin/'
driver = BasePage.Base(browser='chrome')

@pytest.mark.login
# 参数化数据
@pytest.mark.parametrize("logindict", [cases_success])
@allure.description("测试用户登录功能，预期用户能够成功登录系统。")
@pytest.mark.flaky(retries=1, delay=1)
def test_login_in(logindict):
    driver.open_url(url)
    account = logindict["account"]
    password = logindict["password"]
    login_input = driver.find_id('id_username').send_keys(account)
    pwd_input = driver.find_id('id_password').send_keys(password)
    sub_input= driver.find_xpath('//*[@id="login-form"]/div[3]/input').click()


@pytest.mark.add
# 参数化数据
@pytest.mark.parametrize("addict", [cases_add_group])
@allure.description("group添加成功。")
@pytest.mark.flaky(retries=1, delay=1)
def test_add_group(addict):
    groupname = addict["account"]
    expected = addict["expected"]
    add_button = driver.find_class('addlink').click()
    groupname_input = driver.find_xpath('//*[@id="id_name"]').send_keys(groupname)
    save_button = driver.find_xpath('//*[@id="group_form"]/div/div/input[1]').click()
    group_content= driver.find_xpath('//*[@id="auth-group"]').click()
    a_content = driver.find_xpath('//*[@id="content-start"]/ul/li').text
    assert expected in a_content
    driver.driver_close()

