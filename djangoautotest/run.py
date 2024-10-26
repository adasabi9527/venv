import pytest
import os
import allure

if __name__ == '__main__':
    # 指定 Allure 结果存储目录
    allure_results_dir = ('/Users/kika/path/to/venv/djangoautotest/log')

    # 执行 pytest 测试用例
    pytest_args = ['-s', '-v', '--alluredir', allure_results_dir, 'tests']
    pytest.main(pytest_args)

    # 生成 Allure 报告
    allure_report_dir = '/Users/kika/path/to/venv/djangoautotest/reports'
    os.system(f'allure generate {allure_results_dir} -o {allure_report_dir} --clean')

    # 打开 Allure 报告
    os.system(f'allure open {allure_report_dir}')