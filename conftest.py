"""pytest 全局夹具：注入请求客户端与各个 API 资源对象。"""
import pytest

from common.request_helper import RequestHelper
from config import settings


@pytest.fixture(scope="session")
def client():
    helper = RequestHelper(
        base_url=settings.BASE_URL,
        timeout=settings.TIMEOUT,
        headers=settings.DEFAULT_HEADERS,
    )
    yield helper
    helper.session.close()


def _make_api(client, resource: str):
    from core.base_api import BaseAPI

    return BaseAPI(client, resource)


@pytest.fixture
def users_api(client):
    return _make_api(client, "users")


@pytest.fixture
def posts_api(client):
    return _make_api(client, "posts")
