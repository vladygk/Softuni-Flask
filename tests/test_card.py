from managers.cards import CardManager
from models import RoleType, Card
from tests.base import TestRESTAPIBase, generate_token, mock_uuid
from tests.factory import UserFactory, CardFactory
from tests.helpers import card_schema_with_empty_raises_res


class TestCardSchema(TestRESTAPIBase):
    def test_required_fields_missing_raises(self):
        admin = UserFactory(role=RoleType.admin)
        token = generate_token(admin)
        headers = {
            "Authorization": token,
            "Content-Type": "application/json",
        }

        data = {}
        res = self.client.post("/cards", headers=headers, json=data)

        assert res.status_code == 400
        assert res.json == card_schema_with_empty_raises_res




# TODO test create works correctly in the other file