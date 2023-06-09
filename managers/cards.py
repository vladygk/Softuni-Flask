import os.path
import uuid

from werkzeug.exceptions import BadRequest, Forbidden, NotFound

from db import db
from managers.auth import auth
from models import Card
from services.firebase import FirebaseService
from utils.working_with_files import decode_photo

fire_base = FirebaseService()


class CardManager:
    # returns all cards in db
    @staticmethod
    def get_all_for_admin():
        return Card.query.filter_by().all()

    # returns only cards created by specific user
    @staticmethod
    def get_all_for_user():
        current_user = auth.current_user()
        cards = Card.query.filter_by(owner_id=current_user.id).all()
        return cards

    # returns one card in db
    @staticmethod
    def get_one_for_admin(id_):
        card = Card.query.filter_by(id=id_).first()
        if not card:
            raise BadRequest("Card with this id doesn't exist")
        return card

    # returns one card in db if user is the owner
    @staticmethod
    def get_one_for_user(id_):
        current_user = auth.current_user()
        card = Card.query.filter_by(id=id_).first()
        if not card or current_user.id != card.owner_id:
            raise NotFound("Card with this id doesn't exist")
        return card

    @staticmethod
    def create_card(card_data):
        current_user = auth.current_user()
        card_data["owner_id"] = current_user.id

        photo_name = f"{str(uuid.uuid4())}.{card_data.pop('photo_extension')}"
        path_to_store_photo = photo_name
        photo_as_string = card_data.pop("photo_base64")
        decode_photo(path_to_store_photo, photo_as_string)

        try:
            url = fire_base.upload_file(path_to_store_photo, photo_name)
        except Exception as ex:
            raise Exception("Upload to Firebase failed")
        finally:
            os.remove(path_to_store_photo)

        card_data["photo_url"] = url

        card = Card(**card_data)

        db.session.add(card)
        db.session.commit()

        return card

    @staticmethod
    def edit_card_for_admin(card_data, id_):

        card_to_edit = Card.query.filter_by(id=id_).first()
        if not card_to_edit:
            raise NotFound("Invalid card")

        Card.query.filter_by(id=id_).update({'title': card_data["title"],
                                             'description': card_data["description"],
                                             'attribute': card_data["attribute"]
                                             })

        db.session.commit()

        return card_to_edit

    @staticmethod
    def edit_card_for_user(card_data, id_):
        current_user = auth.current_user()

        card_to_edit = Card.query.filter_by(id=id_).first()
        if not card_to_edit:
            raise NotFound("Invalid card")

        if card_to_edit.owner_id != current_user.id:
            raise Forbidden("No access")

        Card.query.filter_by(id=id_).update({'title': card_data["title"],
                                             'description': card_data["description"],
                                             'attribute': card_data["attribute"]
                                             })
        db.session.commit()

        return card_to_edit

    @staticmethod
    def delete_card_for_admin(id_):

        card_to_delete = Card.query.filter_by(id=id_).first()
        if not card_to_delete:
            raise NotFound("Invalid card")

        Card.query.filter_by(id=id_).delete()

        db.session.commit()

        return card_to_delete

    @staticmethod
    def delete_card_for_user(id_):
        current_user = auth.current_user()

        card_to_delete = Card.query.filter_by(id=id_).first()
        if not card_to_delete:
            raise NotFound("Invalid card")

        if card_to_delete.owner_id != current_user.id:
            raise Forbidden("No access")

        Card.query.filter_by(id=id_).delete()

        db.session.commit()

        return card_to_delete
