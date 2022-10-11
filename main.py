import pytest
import os
from common.mysql import delete_test_user
pytest.main([os.path.abspath('testcase/test_g50JHregiser.py'),os.path.abspath('testcase/test_g50regiser.py')])
pytest.main(["-s","-v","--alluredir=allure-report-file"])
os.system('allure generate ./allure-report-file -o ./report --clean')
delete_test_user