"""
    登录测试用例
"""
cases_success = {"account":"admin", "password":"12345678","expected": "WELCOME, ADMIN."}

cases_error1 = {"account1": "admin", "password1": "123", "expected1": "Please enter the correct username and password for a staff account. Note that both fields may be case-sensitive."}

case_error2 = {"account2": "123", "password2": "123", "expected2": "Please enter the correct username and password for a staff account. Note that both fields may be case-sensitive."}

case_error3 = {"account3": "", "password3": "", "expected3": "请填写此字段"}

