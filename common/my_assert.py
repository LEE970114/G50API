"""
======================
Author: 柠檬班-小简
Time: 2021/4/26 21:17
Project: day6
Company: 湖南零檬信息技术有限公司
======================
"""
import ast
from common.logger import logger


class MyAssert:

    def assert_response(self,check_str, response_dict):
        check_res = []
        check_list =ast.literal_eval(check_str)
        for check in check_list:
            logger.info("要断言的内容为：\n{}".format(check))
            res=check in response_dict
            if check not in response_dict:
                logger.info("键值的%s:%s"%(check))
            check_res.append(res)
        if False in check_res:
            logger.error("部分断言失败！，请查看比对结果为False的")
            raise AssertionError
        else:
            logger.info("所有断言成功！")
