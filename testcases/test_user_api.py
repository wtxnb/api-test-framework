"""用户模块接口测试。"""
import allure
import pytest

from common.assertions import AssertHelper
from common.data_loader import load_yaml

cases = load_yaml("users.yaml")["cases"]


@allure.epic("用户模块接口")
@allure.feature("用户查询")
class TestUserApi:
    @allure.story("获取用户列表")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.smoke
    def test_get_users_list(self, users_api):
        resp = users_api.list()
        AssertHelper.status_code(resp, 200)
        AssertHelper.response_time(resp, 3000)
        data = resp.json()
        assert isinstance(data, list) and len(data) > 0

    @allure.story("按 ID 获取单个用户")
    @allure.severity(allure.severity_level.NORMAL)
    def test_get_user_by_id(self, users_api):
        resp = users_api.get_by_id(1)
        AssertHelper.status_code(resp, 200)
        AssertHelper.json_field(resp, "id", 1)
        AssertHelper.contains(resp, "email")

    @allure.story("用户字段数据驱动校验")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.parametrize("user_id,expected_name", cases)
    def test_user_field_driven(self, users_api, user_id, expected_name):
        resp = users_api.get_by_id(user_id)
        AssertHelper.status_code(resp, 200)
        AssertHelper.json_field(resp, "name", expected_name)
