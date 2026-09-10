"""帖子模块接口测试（含增、查、改）。"""
import allure
import pytest

from common.assertions import AssertHelper


@allure.epic("帖子模块接口")
@allure.feature("帖子增删改查")
class TestPostApi:
    @allure.story("创建帖子")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.smoke
    def test_create_post(self, posts_api):
        payload = {"title": "foo", "body": "bar", "userId": 1}
        resp = posts_api.create(payload)
        AssertHelper.status_code(resp, 201)
        data = resp.json()
        assert data["title"] == payload["title"]
        assert data["userId"] == 1

    @allure.story("按用户 ID 查询帖子")
    @allure.severity(allure.severity_level.NORMAL)
    def test_get_posts_by_user(self, posts_api):
        resp = posts_api.list(params={"userId": 1})
        AssertHelper.status_code(resp, 200)
        data = resp.json()
        assert all(p["userId"] == 1 for p in data)

    @allure.story("更新帖子")
    @allure.severity(allure.severity_level.MINOR)
    def test_update_post(self, posts_api):
        payload = {"title": "updated", "body": "updated body", "userId": 1}
        resp = posts_api.update(1, payload)
        AssertHelper.status_code(resp, 200)
        data = resp.json()
        assert data["title"] == "updated"
