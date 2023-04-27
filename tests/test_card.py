from unittest.mock import patch

from models import RoleType, Card
from services.firebase import FirebaseService
from tests.base import TestRESTAPIBase, generate_token, mock_uuid
from tests.factory import UserFactory
from tests.helpers import card_schema_with_empty_raises_res
from tests.helpers import encoded_photo


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


class TestCards(TestRESTAPIBase):
    @patch("uuid.uuid4", mock_uuid)
    @patch.object(FirebaseService, "upload_file", return_value="some_url.com")
    def test_create_cards(self, mock_fire_base_upload):
        cards = Card.query.all()
        assert len(cards) == 0

        admin = UserFactory(role=RoleType.admin)
        token = generate_token(admin)
        headers = {
            "Authorization": token,
            "Content-Type": "application/json",
        }

        data = {
            "description": "test desc",
            "photo_extension": "jpeg",
            "photo_base64": encoded_photo,
            "title": "Test",
            "attribute": "test attr",
        }

        res = self.client.post("/cards", headers=headers, json=data)

        cards = Card.query.all()
        assert len(cards) == 1
        assert res.status_code == 201
        assert res.json["photo_url"] == "some_url.com"

        expected_photo_name = f"{mock_uuid()}.{data['photo_extension']}"
        expected_file_path = f"{mock_uuid()}.{data['photo_extension']}"
        mock_fire_base_upload.assert_called_once_with(expected_file_path, expected_photo_name)
