from models import RoleType
from tests.base import TestRESTAPIBase, generate_token
from tests.factory import UserFactory, CardFactory
from tests.helpers import admin_get_res, user_get_res


class TestLoginAndRoles(TestRESTAPIBase):
    def test_auth_is_required(self):
        # ARRANGE #

        all_guarded_urls = [
            ("GET", "/cards"),
            ("POST", "/cards"),
            ("GET", "/cards/1"),
            ("PUT", "/cards/1"),
            ("DELETE", "/cards/1"),
        ]

        # ACT #

        for method, url in all_guarded_urls:
            if method == "GET":
                res = self.client.get(url)
            elif method == "POST":
                res = self.client.post(url)
            elif method == "PUT":
                res = self.client.put(url)
            else:
                res = self.client.delete(url)

            # ASSERT #
            assert res.status_code == 401
            assert res.json == {'message': 'Invalid or missing token'}

    def test_admin_get_all_cards(self):
        # ARRANGE #

        # create admin user
        admin = UserFactory(role=RoleType.admin)

        # add card by admin
        card_admin1 = CardFactory(owner_id=admin.id)
        card_admin2 = CardFactory(owner_id=admin.id)

        # create user
        user = UserFactory(role=RoleType.user)

        # add card by admin
        card_user1 = CardFactory(owner_id=user.id)
        card_user2 = CardFactory(owner_id=user.id)

        # ACT #

        # generate admin token and make request
        admin_token = generate_token(admin)
        admin_headers = {"Authorization": admin_token}
        admin_res = self.client.get("/cards", headers=admin_headers)

        # ASSERT #

        assert admin_res.status_code == 200
        assert admin_res.json == admin_get_res

    def test_user_get_only_his_cards(self):
        # ARRANGE #

        # create admin user
        admin = UserFactory(role=RoleType.admin)

        # add card by admin
        card_admin1 = CardFactory(owner_id=admin.id)
        card_admin2 = CardFactory(owner_id=admin.id)

        # create user
        user = UserFactory(role=RoleType.user)

        # add card by admin
        card_user1 = CardFactory(owner_id=user.id)
        card_user2 = CardFactory(owner_id=user.id)

        # ACT #

        # generate user token and make request
        user_token = generate_token(user)
        user_headers = {"Authorization": user_token}
        user_res = self.client.get("/cards", headers=user_headers)

        # ASSERT #

        assert user_res.status_code == 200
        assert user_res.json == user_get_res

    def test_admin_edit_any_card(self):
        # ARRANGE #

        # create admin user
        admin = UserFactory(role=RoleType.admin)

        # add card by admin
        card_admin1 = CardFactory(owner_id=admin.id)
        card_admin2 = CardFactory(owner_id=admin.id)

        # create user
        user = UserFactory(role=RoleType.user)

        # add card by admin
        card_user1 = CardFactory(owner_id=user.id)
        card_user2 = CardFactory(owner_id=user.id)

        # generate admin token and make request
        admin_token = generate_token(admin)
        admin_headers = {"Authorization": admin_token}

        edit_data = {
            "photo_url": "edited",
            "title": "Edited ",
            "description": "edited",
            "attribute": "edited"
        }

        admin_created_card_res = self.client.put("/cards/0", headers=admin_headers, json=edit_data)
        user_created_card_res = self.client.put("/cards/2", headers=admin_headers, json=edit_data)

        assert admin_created_card_res.status_code == 200
        assert user_created_card_res.status_code == 200

    def test_user_edit_only_his_card(self):
        # ARRANGE #

        # create admin user
        admin = UserFactory(role=RoleType.admin)

        # add card by admin
        card_admin1 = CardFactory(owner_id=admin.id)
        card_admin2 = CardFactory(owner_id=admin.id)

        # create user
        user = UserFactory(role=RoleType.user)

        # add card by admin
        card_user1 = CardFactory(owner_id=user.id)
        card_user2 = CardFactory(owner_id=user.id)

        # generate user token and make request
        user_token = generate_token(user)
        user_headers = {"Authorization": user_token}

        edit_data = {
            "photo_url": "edited",
            "title": "Edited ",
            "description": "edited",
            "attribute": "edited"
        }

        admin_created_card_res = self.client.put("/cards/0", headers=user_headers, json=edit_data)
        user_created_card_res = self.client.put("/cards/2", headers=user_headers, json=edit_data)

        assert admin_created_card_res.status_code == 403
        assert user_created_card_res.status_code == 200

    def test_admin_delete_any_card(self):
        # ARRANGE #

        # create admin user
        admin = UserFactory(role=RoleType.admin)

        # add card by admin
        card_admin1 = CardFactory(owner_id=admin.id)
        card_admin2 = CardFactory(owner_id=admin.id)

        # create user
        user = UserFactory(role=RoleType.user)

        # add card by admin
        card_user1 = CardFactory(owner_id=user.id)
        card_user2 = CardFactory(owner_id=user.id)

        # generate admin token and make request
        admin_token = generate_token(admin)
        admin_headers = {"Authorization": admin_token}

        edit_data = {
            "photo_url": "edited",
            "title": "Edited ",
            "description": "edited",
            "attribute": "edited"
        }

        admin_created_card_res = self.client.delete("/cards/0", headers=admin_headers, json=edit_data)
        user_created_card_res = self.client.delete("/cards/2", headers=admin_headers, json=edit_data)

        assert admin_created_card_res.status_code == 200
        assert user_created_card_res.status_code == 200

    def test_user_delete_only_his_card(self):
        # ARRANGE #

        # create admin user
        admin = UserFactory(role=RoleType.admin)

        # add card by admin
        card_admin1 = CardFactory(owner_id=admin.id)
        card_admin2 = CardFactory(owner_id=admin.id)

        # create user
        user = UserFactory(role=RoleType.user)

        # add card by admin
        card_user1 = CardFactory(owner_id=user.id)
        card_user2 = CardFactory(owner_id=user.id)

        # generate user token and make request
        user_token = generate_token(user)
        user_headers = {"Authorization": user_token}

        edit_data = {
            "photo_url": "edited",
            "title": "Edited ",
            "description": "edited",
            "attribute": "edited"
        }

        admin_created_card_res = self.client.delete("/cards/0", headers=user_headers, json=edit_data)
        user_created_card_res = self.client.delete("/cards/2", headers=user_headers, json=edit_data)

        assert admin_created_card_res.status_code == 403
        assert user_created_card_res.status_code == 200



