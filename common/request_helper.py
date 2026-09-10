"""请求封装层：对 requests 做统一封装，自动记录日志并把请求/响应
以 Allure 附件形式保留，方便在报告中排查问题。"""
import allure
from typing import Optional

import requests
from common.logger import get_logger

logger = get_logger("request_helper")


class RequestHelper:
    def __init__(self, base_url: str, timeout: int = 10, headers: Optional[dict] = None):
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
        self.session = requests.Session()
        if headers:
            self.session.headers.update(headers)

    def request(self, method: str, path: str, **kwargs):
        url = f"{self.base_url}/{path.lstrip('/')}"
        attach_text = f"{method} {url}\nkwargs={kwargs}"
        allure.attach(attach_text, name="Request", attachment_type=allure.attachment_type.TEXT)
        logger.info("%s %s", method, url)
        resp = self.session.request(method, url, timeout=self.timeout, **kwargs)
        allure.attach(
            resp.text, name="Response", attachment_type=allure.attachment_type.TEXT
        )
        logger.info("-> status=%s cost=%.0fms", resp.status_code, resp.elapsed.total_seconds() * 1000)
        return resp

    def get(self, path, **kwargs):
        return self.request("GET", path, **kwargs)

    def post(self, path, **kwargs):
        return self.request("POST", path, **kwargs)

    def put(self, path, **kwargs):
        return self.request("PUT", path, **kwargs)

    def patch(self, path, **kwargs):
        return self.request("PATCH", path, **kwargs)

    def delete(self, path, **kwargs):
        return self.request("DELETE", path, **kwargs)
