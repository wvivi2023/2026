import requests
from config.settings import BASE_URL, HEADERS, TOKEN_DATA
from common.logger import log

class RequestUtil:
    @staticmethod
    def send_request(method, url, params=None, json=None):
        full_url = BASE_URL + url
        headers = HEADERS.copy()

        # 自动携带Token
        token = TOKEN_DATA["token"]
        if token:
            headers["Authorization"] = f"Bearer {token}"

        log.info(f"请求地址: {full_url}")
        log.info(f"请求头: {headers}")
        log.info(f"请求参数: {json if json else params}")

        try:
            if method.upper() == "GET":
                resp = requests.get(full_url, headers=headers, params=params, timeout=10)
            elif method.upper() == "POST":
                resp = requests.post(full_url, headers=headers, json=json, timeout=10)
            else:
                raise Exception("不支持的请求方法")

            log.info(f"响应状态码: {resp.status_code}")
            log.info(f"响应数据: {resp.text}")
            return resp
        except Exception as e:
            log.error(f"请求异常: {str(e)}")
            raise