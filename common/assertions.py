"""断言封装层：所有断言都包裹在 Allure step 中，失败时能清晰定位。"""
import allure


class AssertHelper:
    @staticmethod
    def status_code(resp, expected: int):
        with allure.step(f"断言状态码 == {expected}"):
            assert resp.status_code == expected, (
                f"期望状态码 {expected}，实际 {resp.status_code}"
            )

    @staticmethod
    def json_field(resp, field: str, expected):
        data = resp.json()
        actual = data.get(field) if isinstance(data, dict) else None
        with allure.step(f"断言字段 {field} == {expected!r}"):
            assert actual == expected, (
                f"字段 {field} 期望 {expected!r}，实际 {actual!r}"
            )

    @staticmethod
    def contains(resp, key: str):
        data = resp.json()
        with allure.step(f"断言响应包含字段 {key}"):
            assert key in data, f"响应中未包含字段 {key}"

    @staticmethod
    def body_equals(resp, expected: dict):
        data = resp.json()
        with allure.step("断言响应体等于预期"):
            assert data == expected, f"响应体不一致:\n实际 {data}\n预期 {expected}"

    @staticmethod
    def response_time(resp, max_ms: int = 2000):
        cost = resp.elapsed.total_seconds() * 1000
        with allure.step(f"断言响应时间 < {max_ms}ms (实际 {cost:.0f}ms)"):
            assert cost < max_ms, f"响应过慢: {cost:.0f}ms"
