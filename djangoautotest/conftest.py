# 文件名必须这个，不能改。
# 钩子函数都是框架自带的。pytest的钩子函数

import pytest
import logging


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    # 通过 out = yield 定义了一个生成器。在生成器中，res = out.get_result() 获取了测试结果对象。
    out = yield  # 类似于return，但是它返回之后执行完毕会自动回来
    res = out.get_result()
    #  res.when == "call"：表示正在运行调用测试函数的阶段。
    if res.when == "call":
        logging.info(f"用例ID：{res.nodeid}")
        logging.info(f"测试结果：{res.outcome}")
        logging.info(f"故障表示：{res.longrepr}")
        logging.info(f"异常：{call.excinfo}")
        logging.info(f"用例耗时：{res.duration}")
        logging.info("**************************************")
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler('/Users/kika/path/to/venv/djangoautotest/log/pytest_log.log')])