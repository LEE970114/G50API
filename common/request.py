import json
import requests
from testcase.config import MyConf
conf=MyConf("testcase/conf_test.ini")
class Test_requests:
    def Res(self,method,URL,data):
        if method.upper()=="GET":
            response = requests.request(method=method, url=URL, json=data,headers=json.loads(conf.get("headers","header")))
        else:
            response = requests.request(method=method, url=URL, json=data,headers=json.loads(conf.get("headers","header")))
        return response
