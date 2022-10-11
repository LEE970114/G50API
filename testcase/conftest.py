import json
import requests
import pytest
from testcase.config import MyConf
config=MyConf("testcase/conf_test.ini")
@pytest.fixture(scope="session")
def get_token():
    token=requests.post("%s"%config.get("token","url"),json=json.loads(config.get("token","data"))).json()["data"]["token"]
    return token
@pytest.fixture(scope="session")
def get_token2():
    token2 = requests.post("%s"%config.get("token2", "url"),
                           json=json.loads(config.get("token2", "data"))).json()["body"]["token"]
    return token2
