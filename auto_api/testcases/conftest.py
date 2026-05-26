import pytest
from common.request_util import RequestUtil
from config.settings import TEST_USER, TOKEN_DATA

# 会话级夹具：全局前置登录获取Token，自动执行
@pytest.fixture(scope="session", autouse=True)
def get_login_token():
    login_url = "/login"
    data = {
        "username": TEST_USER["username"],
        "password": TEST_USER["password"]
    }
    resp = RequestUtil.send_request("POST", login_url, json=data)
    assert resp.status_code == 200
    token = resp.json().get("token")
    assert token is not None

    # 赋值Token，供后续接口使用
    TOKEN_DATA["token"] = token
    yield
    print("所有测试用例执行完毕")