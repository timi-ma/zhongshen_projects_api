import os

import pytest

pytest.main(["./testcases_众神_接口测试",
             "-sv", "--alluredir", "./testoutput_测试报告/temp"])
os.system("allure generate ./testoutput_测试报告/temp -o ./testoutput_测试报告/html --clean")