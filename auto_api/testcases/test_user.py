from common.request_util import RequestUtil

class TestUserInfo:
    def test_get_user_info(self):
        """获取用户信息（需Token鉴权）"""
        url = "/user/info"
        resp = RequestUtil.send_request("GET", url)
        assert resp.status_code == 200
        assert "username" in resp.json()