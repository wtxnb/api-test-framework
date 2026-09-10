"""API 资源基类：把某个 RESTful 资源（users / posts ...）的通用
增删改查封装起来，测试用例直接调用语义化方法。"""


class BaseAPI:
    def __init__(self, client, resource: str):
        self.client = client
        self.resource = resource

    def list(self, **kwargs):
        return self.client.get(self.resource, **kwargs)

    def get_by_id(self, _id, **kwargs):
        return self.client.get(f"{self.resource}/{_id}", **kwargs)

    def create(self, payload: dict, **kwargs):
        return self.client.post(self.resource, json=payload, **kwargs)

    def update(self, _id, payload: dict, **kwargs):
        return self.client.put(f"{self.resource}/{_id}", json=payload, **kwargs)

    def patch(self, _id, payload: dict, **kwargs):
        return self.client.patch(f"{self.resource}/{_id}", json=payload, **kwargs)

    def delete(self, _id, **kwargs):
        return self.client.delete(f"{self.resource}/{_id}", **kwargs)
