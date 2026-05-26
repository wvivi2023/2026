import pytest
from common.request_util import RequestUtil
from config.settings import TEST_USER

class TestLogin:
    def test_login_success(self):
        """正常登录-正向用例"""
        url = "/login"
        data = {
            "username": TEST_USER["username"],
            "password": TEST_USER["password"]
        }
        resp = RequestUtil.send_request("POST", url, json=data)
        assert resp.status_code == 200
        assert "token" in resp.json()

    @pytest.mark.parametrize("user,pwd,code", [
        ("admin", "wrong", 401),
        ("", "123456", 401)
    ])
    def test_login_fail(self, user, pwd, code):
        """参数化-异常登录用例"""
        url = "/login"
        data = {"username": user, "password": pwd}
        resp = RequestUtil.send_request("POST", url, json=data)
        assert resp.status_code == code