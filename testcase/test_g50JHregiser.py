import json
import os
from common.excel_read import Open_Excel
from common.request import Test_requests
import pytest
import allure
from common.logger import logger
from common.my_assert import MyAssert
path = os.path.abspath('.')
excel_name = os.path.join(path,'data/g50test_data.xlsx')
cases=Open_Excel().read_data(excel_name,"聚合服务器")
@allure.feature("聚合路由器模块")
class TestRegiser:

    @pytest.mark.parametrize("case",cases)
    def test_regiser(self,case,get_token2):
        if case["req_data"] and case["req_data"].find('#token2#') != -1:
            case["req_data"] = case["req_data"].replace('#token2#', get_token2)
        if case["assert_list"] and case["assert_list"].find('#token2#') != -1:
            case["assert_list"] = case["assert_list"].replace('#token2#',get_token2)
        req_dict = json.loads(case["req_data"])
        response = Test_requests().Res(case["method"], case["url"], req_dict)
        logger.info(case)
        logger.info("测试参数\n%s"%req_dict)
        logger.info("响应信息\n%s"%response.json())
        MyAssert().assert_response(case["assert_list"],response.json())













